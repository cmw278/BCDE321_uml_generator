class DotAssociation:

    def __init__(self, class_: str, target_class: str, label: str = ''):
        self.my_class = class_
        self.target_class = target_class
        self.label = label

    def __str__(self):
        return ('\n%s -> %s' % (self.target_class, self.my_class)
                + self._get_options())

    def _get_options(self) -> str:
        if self._has_options():
            options = '\n['
            for option in self._options():
                options = options + option
            return options + ']'
        else:
            return ''

    def _has_options(self) -> bool:
        return self.label != ''

    def _options(self):
        yield '\nlabel="%s"' % self.label
