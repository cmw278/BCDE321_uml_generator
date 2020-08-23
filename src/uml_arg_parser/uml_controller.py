from graphviz_uml import GraphvizUML
from pathlib import Path
from pkg_resources import resource_filename
import logging
import logging.config
import traceback
import json

config_file = resource_filename(__name__, 'data/logging.conf')
logging.config.fileConfig(config_file)
log = logging.getLogger('Get-UML')


class UMLController:
    def __init__(self):
        log.info('System initialising...')
        self._js_dict = None
        self._uml_generator = None

    def handle_args(self, args: object) -> None:
        if args.verbose:
            log.setLevel(logging.DEBUG)
        elif args.quiet:
            log.setLevel(logging.WARN)
        log.debug('Handling command line arguments')
        log.debug('Arguments received:\n\n%s\n' % args)
        targetfile = str(args.source)
        try:
            if not args.json:
                log.debug('Processing as JavaScript source')
                self.load_file(targetfile)
            else:
                log.debug('Processing as JSON source')
                self.load_json(targetfile)
            cleanup = not args.save_dot
            log.debug('%s DOT source file...'
                      % ('Not keeping' if cleanup else 'Keeping'))
            if args.view:
                self.view_uml(filename=args.name, directory=args.destination,
                              format=args.format, cleanup=cleanup)
            else:
                self.save_file(filename=args.name, directory=args.destination,
                               format=args.format, cleanup=cleanup)
        except Exception as error:
            log.critical(
                'Operation failed with the following error:\n\n%s\n'
                % str(error))
            log.debug(traceback.format_exc())
            log.critical('Exiting now.')
            exit()

    def load_file(self, targetfile: str) -> None:
        """Load a file into memory and prepare it for generating a UML 2
        class diagram.

        ---
        Required Positional Arguments:

        `[0] targetfile: str`
        > The path to the file you wish to open. Can be
        a relative or absolute path.
        """
        path = Path(targetfile)
        log.info('Attempting to read from %s' % path)
        raise NotImplementedError(
            'WIP: This interface has not been implemented yet')
        if not path.is_dir():
            pass
        elif path.is_dir():
            pass

    def load_json(self, targetfile: str) -> None:
        """Load a JSON file and prepare it for generating a UML 2
        class diagram.

        ---
        Required Positional Arguments:

        `[0] targetfile: str`
        > The path to the JSON file you wish to open. Can be
        a relative or absolute path.
        """
        log.info('Reading %s as JSON' % targetfile)
        file_ = open(targetfile)
        self._js_dict = json.load(file_)

    def run_analysis(self) -> str:
        """Generate the DOT formatted string for the currently loaded file.

        ---
        `returns -> str`
        > The DOT formatted string.
        """
        self._get_uml_generator()
        return str(self._uml_generator)

    def save_file(self, *, filename: str = None, directory: str = None,
                  format: str = 'png', cleanup: bool = True) -> None:
        """Save the generated UML 2 class diagram.

        ---
        Optional Keyword Arguments:

        `filename: str`
        > The destination filename (without the extension).
        Defaults to the name of the directory or file the UML is generated
        from.

        `directory: str`
        > The destination directory where output will be saved.
        Defaults to the current working directory.

        `format: str`
        > The desired file format of the generated UML.
        Common formats include: png, bmp, jpeg, gif, svg, and pdf.
        Defaults to png.

        `cleanup: bool`
        > Specify whether to remove generated DOT source file.
        Default = `True`
        """
        self._get_uml_generator()
        output_path = self._uml_generator.render(
            filename=filename,
            directory=directory,
            format=format,
            cleanup=cleanup
        )
        log.info('Diagram saved to %s' % output_path)

    def view_uml(self, *, filename: str = None, directory: str = None,
                 format: str = 'png', cleanup: bool = True) -> None:
        """Saves the generated UML 2 class diagram and opens the resulting
        file for preview.

        ---
        Optional Keyword Arguments:

        `filename: str`
        > The destination filename (without the extension).
        Defaults to the name of the directory or file the UML is generated
        from.

        `directory: str`
        > The destination directory where output will be saved.
        Defaults to the current working directory.

        `format: str`
        > The desired file format of the generated UML.
        Common formats include: png, bmp, jpeg, gif, svg, and pdf.
        Defaults to png.

        `cleanup: bool`
        > Specify whether to remove generated DOT source file.
        Default = `True`
        """
        self._get_uml_generator()
        log.debug('Saving diagram...')
        output_path = self._uml_generator.view(
            filename=filename,
            directory=directory,
            format=format,
            cleanup=cleanup
        )
        log.info('Diagram saved to %s, opening now...' % output_path)

    def _get_uml_generator(self) -> None:
        """Intantiate `GraphvizUML` class using stored `dict`.

        ---
        Will create an instance of GraphvizUML using `self._js_dict`. If
        `self._js_dict` is unset, an `AssertionError` will be raised.

        The GraphvizUML instance will be stored in `self._uml_generator`.
        """
        assert self._js_dict is not None, """You must open a file before
        this operation can be performed.
        """
        log.debug('Generating UML DOT source...')
        self._uml_generator = GraphvizUML(self._js_dict)