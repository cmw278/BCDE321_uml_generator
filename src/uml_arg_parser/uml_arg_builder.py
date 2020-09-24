from argparse import ArgumentParser, RawDescriptionHelpFormatter
from pkg_resources import resource_string
from pathlib import Path


class UMLArgBuilder:

    def __init__(self):
        self.build = {
            'load':    self.build_load_parser,
            'analyze': self.build_analyze_parser,
            'save':    self.build_save_parser,
            'set':     self.build_set_parser
        }

    def help(self, subject: str) -> str:
        return resource_string(__name__, 'data/%s.help' % subject).decode()

    def get_new_parser(self, name: str) -> ArgumentParser:
        return ArgumentParser(
            prog=name,
            description=self.help(name),
            epilog=self.help('epilog'),
            formatter_class=RawDescriptionHelpFormatter,
            allow_abbrev=True,
            add_help=False)

    def build_parser(self, name: str) -> (str, ArgumentParser):
        parser = self.get_new_parser(name=name)
        self.build[name](parser)
        return name, parser

    def build_load_parser(self, parser: ArgumentParser) -> None:
        self.attach_verbosity(parser)
        parser.add_argument('files', nargs='+', help=self.help('load_files'),
                            type=Path)
        parser.add_argument('--no-recurse', help=self.help('no-recurse'),
                            action='store_true')

    def build_analyze_parser(self, parser: ArgumentParser) -> None:
        self.attach_verbosity(parser)
        parser.add_argument('-j', '--json', help=self.help('json'),
                            action='store_true')

    def build_save_parser(self, parser: ArgumentParser) -> None:
        self.attach_verbosity(parser)
        self.attach_output_arguments(parser)
        parser.add_argument('--view', help=self.help('view'),
                            action='store_true')

    def build_set_parser(self, parser: ArgumentParser) -> None:
        self.attach_output_arguments(parser)
        parser.add_argument('--log-level', help=self.help('log-level'),
                            choices=['DEBUG', 'INFO', 'WARNING',
                                     'ERROR', 'CRITICAL'])

    def attach_verbosity(self, parser: ArgumentParser) -> None:
        verbosity = parser.add_mutually_exclusive_group()
        verbosity.add_argument('-q', '--quiet', help=self.help('quiet'),
                               action='store_true')
        verbosity.add_argument('-v', '--verbose', help=self.help('verbose'),
                               action='store_true')

    def attach_output_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument('--name', help=self.help('name'))
        parser.add_argument('--destination', help=self.help('destination'))
        parser.add_argument('--format', help=self.help('format'))
