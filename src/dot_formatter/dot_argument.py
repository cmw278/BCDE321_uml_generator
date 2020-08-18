from dot_formatter import DotObject


class DotArgument(DotObject):

    def __init__(self, name: str, type_: str):
        super().__init__(name)
        self.type = type_

    def __str__(self) -> str:
        return '%s: %s' % (self.name, self.type)
