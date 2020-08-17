from dot_formatter import DotAssociation


class DotInheritance(DotAssociation):

    def _set_options(self, label: str, arrowtail: str = 'empty') -> None:
        # Override to introduce the arrowtail option, which defaults
        # to `empty` (arrow outline) for inheritance relationship.
        self.options = {
            'label': label,
            'arrowtail': arrowtail
        }
