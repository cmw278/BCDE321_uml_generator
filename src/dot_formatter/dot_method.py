from dot_formatter import DotObject, DotArgument


class DotMethod(DotObject):

    def __init__(self, name: str, return_type: str = None):
        super().__init__(name)
        self.return_type = return_type
        self.all_my_arguments = []

    def add_argument(self, argument_name: str,
                     argument_type: str) -> DotArgument:
        new_argument = DotArgument(argument_name, argument_type)
        self.all_my_arguments.append(new_argument)
        return new_argument

    def __str__(self) -> str:
        arguments = (
            ', '.join([str(argument) for argument in self.all_my_arguments])
        )
        return '+ %s(%s)%s\\l' % (
            self.name,
            arguments,
            (': %s' % self.return_type) if self.return_type is not None else ''
        )
