from argparse import ArgumentParser, RawDescriptionHelpFormatter, Namespace
from pkg_resources import resource_string
from uml_arg_parser import UMLController


class UMLArgParser(ArgumentParser):
    """A wrapper for ArgumentsParser that defines and processes arguments for
    `uml-generator`
    """
    def __init__(self):
        super().__init__(
            description=self._help('description'),
            epilog=self._help('epilog'),
            formatter_class=RawDescriptionHelpFormatter)

        self._add_required_arguments()
        self._add_optional_arguments()
        self._uml_controller = UMLController()

    def parse_args(self, args: list = None) -> None:
        args = super().parse_args(args)
        self._go(args)

    def _help(self, subject: str) -> str:
        return resource_string(__name__, 'data/%s.help' % subject).decode()

    def _add_required_arguments(self) -> None:
        self.add_argument('source', help=self._help('source'))

    def _add_optional_arguments(self) -> None:
        verbosity = self.add_mutually_exclusive_group()
        verbosity.add_argument('-q', '--quiet', help=self._help('quiet'),
                               action='store_true')
        verbosity.add_argument('-v', '--verbose', help=self._help('verbose'),
                               action='store_true')
        self.add_argument('--view', help=self._help('view'),
                          action='store_true')
        self.add_argument('-n', '--name', help=self._help('name'))
        self.add_argument('-f', '--format', help=self._help('format'),
                          default='png'),
        self.add_argument('--destination', help=self._help('destination'))
        self.add_argument('--save-dot', help=self._help('save-dot'),
                          action='store_true')
        self.add_argument('-j', '--json', help=self._help('json'),
                          action='store_true')
        self.add_argument('--version', help=self._help('version'),
                          action='version', version=self._help('version'))

    def _go(self, args: Namespace) -> None:
        self._uml_controller.handle_args(args)

if __name__ == '__main__':
    parser = UMLArgParser()
    parser.parse_args()