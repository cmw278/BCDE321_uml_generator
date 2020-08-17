class DotAssociation:

    def __init__(self, class_: str, target_class: str, label: str = ''):
        self.my_class = class_
        self.target_class = target_class
        self.label = label

    def __str__(self):
        return ('\n%s -> %s' % (self.target_class, self.my_class)
                + self._get_options())

    def _get_options(self) -> str:
        return ' [\n%s\n]' % '\n'.join(
            ['%s="%s"' % (key, value) for key, value in self._options()]
        )

    def _options(self):
        yield ('label', self.label)
