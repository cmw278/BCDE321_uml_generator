from graphviz_uml import GraphvizUML
from js_analyzer import JsAnalyzer
from pathlib import Path
from argparse import Namespace
from pkg_resources import resource_filename
from .abstract_view import AbstractView
import logging
import traceback
import json
import re

log = logging.getLogger('Get-UML')


class CmdController:

    def __init__(self, view: AbstractView):
        log.info('System initialising...')
        self.view = view
        self.reset()
        self._actions = {
            'load': self.load,
            'analyze': self.analyze,
            'save': self.save
        }
        self._supported_filetypes = [
            '.js',
            '.json'
        ]

    def reset(self) -> None:
        log.debug('Resetting data.')
        self._js_dict = {}
        self._paths = set()
        self._opts = {
            'name': '',
            'destination': None,
            'format': 'pdf',
            'log_level': 'INFO'
        }

    @property
    def name(self) -> str:
        return self._opts['name']

    @name.setter
    def name(self, value: str) -> None:
        self._opts['name'] = re.sub('[^\\w]', '', value)

    def set_opts(self, opts: Namespace) -> None:
        for key, value in vars(opts).items():
            if value is not None:
                self._opts[key] = value
        self.name = self.name
        self.refresh_log_level()

    def refresh_log_level(self) -> None:
        self.view.set_log_level(self._opts['log_level'])

    def set_temp_log_level(self, args: Namespace) -> None:
        if args.verbose:
            self.view.set_log_level('DEBUG')
        elif args.quiet:
            self.view.set_log_level('WARNING')

    def perform_action(self, action: str, args: Namespace) -> None:
        assert action in self._actions.keys()
        self.set_temp_log_level(args)
        try:
            self._actions[action](args)
        except NotImplementedError:
            log.critical(f'{action} is not yet supported with'
                         ' the provided options')
        finally:
            self.refresh_log_level()

    def load(self, args: Namespace) -> None:
        [self.scan_path(target, args.no_recurse) for target in args.files]
        if len(self._paths) == 0:
            log.warning('No supported files have been found.'
                        ' Please load supported files.')

    def scan_path(self, path: Path, norecurse: bool = False) -> None:
        """Scan a file or directory into memory to prepare for generating
        a UML 2 class diagram.

        ---
        Required Positional Arguments:

        `[0] path: Path`
        > The path to the file or directory you wish to scan. Can be
        a relative or absolute path.

        `[1] norecurse: bool`
        > A boolean flag indicating not to scan recursively.
        """
        log.debug('Loading path %s' % path)
        if len(self.name) == 0:
            self.name = path.stem

        if not path.is_dir():
            self.load_file(path)
        elif path.is_dir() and not norecurse:
            [self.scan_path(next_path) for next_path in path.iterdir()]

    def load_file(self, path: Path) -> None:
        """Load a file into memory to prepare it for generating a UML 2
        class diagram.

        ---
        Required Positional Arguments:

        `[0] path: Path`
        > The path to the file you wish to load. Can be
        a relative or absolute path.
        """
        if path.suffix.lower() in self._supported_filetypes:
            log.debug(f'Found `{path}`')
            self._paths.add(path)
        else:
            log.debug(f'Unsupported filetype: `{path.suffix}`. '
                      f'`{path}` has not been loaded.')

    def analyze(self, args: Namespace) -> None:
        """Start the JavaScript analyzer and analyze target file(s).

        ---
        Required Positional Arguments:

        `[0] args: Namespace`
        > The arguments provided by the argparse module.
        """
        if len(self._paths) == 0:
            log.warning('No files selected. Please select files using'
                        ' `load`. see `help load` for details.')
            return None
        if args.json:
            return self.load_json()
        analyzer = JsAnalyzer(self.name)
        [analyzer.load_file(path) for path in self._paths]
        self._js_dict = analyzer.to_dict()
        self.analyzer_status()

    def load_json(self) -> None:
        """Load a JSON file and prepare it for generating a UML 2
        class diagram.
        """
        log.info('Analyzing JSON files')
        for path in self._paths:
            if path.suffix.lower() == '.json':
                self._js_dict = {
                    **self._js_dict,
                    **json.load(path.open())
                }
        self.analyzer_status()

    def analyzer_status(self) -> None:
        if len(self._js_dict.keys()) <= 0:
            log.warning('No data was loaded, please check data source.')
            return None
        log.debug('Found data structure: %s\n', json.dumps(
            self._js_dict,
            sort_keys=True,
            indent=2
        ))

    def save(self, args: Namespace) -> None:
        """Save the generated UML 2 class diagram.
        """
        if len(self._js_dict.keys()) <= 0:
            log.warning('No existing data, please perform an analysis.')
            return None
        opts = self._parse_opts(args)

        log.info('Generating UML')
        if opts['view']:
            log.info('Diagram will open automagically.')
        formatter = GraphvizUML(self._js_dict)
        try:
            output_path = formatter.render(
                filename=opts['name'],
                directory=opts['destination'],
                format=opts['format'],
                view=opts['view'],
                cleanup=True
            )
            log.info('Diagram saved to %s' % output_path)
        except PermissionError:
            log.critical('Permission denied when saving file. Please try'
                         ' saving using a different name or directory')

    def _parse_opts(self, args: Namespace) -> dict:
        opts = {
            **self._opts
        }
        for key, value in vars(args).items():
            if value is not None:
                opts[key] = value
        return opts
