from . import ClassBuilder


class ClassDirector:
    def __init__(self, builder: ClassBuilder):
        self.builder = builder

    def make_class(self, class_dict: dict) -> None:
        self.builder.new_class(class_dict['name'])
        self._add_attributes(class_dict['attributes'])
        self._add_methods(class_dict['methods'])

    def _add_attributes(self, attributes_array: list) -> None:
        for attr in attributes_array:
            attr_name = attr['name']
            attr_type = None
            if 'type' in attr:
                attr_type = attr['type']

            self.builder.add_attribute(attr_name, attr_type)

    def _add_methods(self, methods_array: list) -> None:
        for method in methods_array:
            method_name = method['name']
            method_return_type = None
            if 'return_type' in method:
                method_return_type = method['return_type']

            self.builder.add_method(method_name, method_return_type)

            if 'arguments' in method:
                self._add_arguments(method['arguments'])

    def _add_arguments(self, args_array: list) -> None:
        for arg in args_array:
            arg_name = arg['name']
            arg_type = None
            if 'type' in arg:
                arg_type = arg['type']

            self.builder.add_argument(arg_name, arg_type)
