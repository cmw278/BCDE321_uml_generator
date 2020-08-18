from dot_formatter import DotRelationship


class DotInheritance(DotRelationship):

    def _set_options(self, label: str, arrowtail: str = 'empty') -> None:
        self.options = {
            'label': label,
            'arrowtail': arrowtail
        }
