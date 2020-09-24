from cmd import Cmd
from .abstract_view import AbstractView
from .cmd_controller import CmdController
from .uml_arg_builder import UMLArgBuilder
from argparse import Namespace, ArgumentParser
import logging


class UMLCmd (Cmd, AbstractView):
    """Command-line interpreter << view >> for UML generator program.
    """

    prompt = 'get-uml >>> '
    parser_names = ['load', 'analyze', 'save', 'set']

    def __init__(self, *args, **kwargs):
        Cmd.__init__(self, *args, **kwargs)
        AbstractView.__init__(self, 'Get-UML')
        self._arg_parsers = {
            key: value for key, value in self.build_arg_parsers()
        }

    def build_arg_parsers(self) -> (str, ArgumentParser):
        builder = UMLArgBuilder()
        self.debug('Building Arguments Parsers.')
        for parser in self.parser_names:
            yield builder.build_parser(parser)

    def _parse_args(self, name: str, argstring: str) -> Namespace:
        args = argstring.split(' ') if len(argstring) > 0 else []
        return self._arg_parsers[name].parse_args(args)

    def show(self, msg: str) -> None:
        print(msg)

    def get_input(self, msg: str = None) -> str:
        input(prompt=msg)

    def set_controller(self, controller: CmdController) -> None:
        self.controller = controller

    def do_load(self, argstring: str) -> None:
        """Load
        """
        self.debug(f'Loading: {argstring}')
        args = self._parse_args('load', argstring)
        self.controller.perform_action('load', args)

    def do_analyze(self, argstring: str) -> None:
        """Analyze
        """
        self.debug(f'Analyzing: {argstring}')
        args = self._parse_args('analyze', argstring)
        self.controller.perform_action('analyze', args)

    def do_save(self, argstring: str = None) -> None:
        """Save
        """
        self.debug(f'Saving: {argstring}')
        args = self._parse_args('save', argstring)
        self.controller.perform_action('save', args)

    def do_set(self, argstring: str) -> None:
        """Set
        """
        self.debug(f'Setting: {argstring}')
        args = self._parse_args('set', argstring)
        self.controller.set_opts(args)

    def do_reset(self, tail: str) -> None:
        """Reset all data.
        """
        self.controller.reset()

    def do_exit(self, tail: str) -> bool:
        """exit [now]
        Exit the program. This will prompt for confirmation before exiting
        the program. Confirmation can be suppressed by issuing `exit now`, or
        by pressing `ctrl + c`.
        """
        if tail == 'now':
            return True
        confirm = self.get_input('Confirm exit ([y] or n): ')
        if len(confirm) == 0 or confirm[0].lower() == 'y':
            return self.onecmd('exit now')
        return False

    def do_help(self, tail: str) -> None:
        """Print help messages and show usage for different commands.
        """
        args = tail.split(' ')
        if args[0] in self._arg_parsers.keys():
            self._arg_parsers[args[0]].print_help()
        else:
            return super().do_help(tail)
