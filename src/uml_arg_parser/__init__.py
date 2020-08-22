from .uml_controller import UMLController
from .uml_arg_parser import UMLArgParser


def get_uml():
    parser = UMLArgParser()
    parser.parse_args()
