from . import DotClass


class ClassBuilder:
    def new_class(self, class_name: str) -> None:
        self._current_class = DotClass(class_name)

    def add_attribute(self, attr_name: str, attr_type: str) -> None:
        self._current_class.add_attribute(attr_name, attr_type)

    def add_method(self, method_name: str, method_return_type: str) -> None:
        self._current_method = self._current_class.add_method(
            method_name, method_return_type
        )

    def add_argument(self, arg_name: str, arg_type: str) -> None:
        self._current_method.add_argument(arg_name, arg_type)

    def get_class(self) -> DotClass:
        return self._current_class
