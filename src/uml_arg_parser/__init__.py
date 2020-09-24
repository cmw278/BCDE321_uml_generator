from .abstract_view import AbstractView
from .cmd_controller import CmdController
from .path_parser import PathParser
from .uml_arg_builder import UMLArgBuilder
from .uml_cmd import UMLCmd


def get_uml():
    view = UMLCmd()
    controller = CmdController(view)
    view.set_controller(controller)

    def go():
        try:
            view.cmdloop()
        except SystemExit:
            go()
        except Exception as e:
            raise e
        except KeyboardInterrupt:
            exit()
    go()
