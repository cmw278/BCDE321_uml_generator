class DotAssociation:

    def __init__(self, source_class: str, target_class: str, label: str = ''):
        self.source_class = source_class
        self.target_class = target_class
        self._set_options(label)

    def _set_options(self, label: str) -> None:
        self.options = {
            'label': label
        }

    def __str__(self):
        return ('\n%s -> %s' % (self.target_class, self.source_class)
                + self._get_options())

    def _get_options(self) -> str:
        return ' [\n%s\n]' % '\n'.join(
            ['%s="%s"' % (key, value) for key, value in self.options.items()]
        )
