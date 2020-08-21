from dot_formatter import DotRelationship


class DotAssociation(DotRelationship):

    def _set_options(self, label: str) -> None:
        self.options = {
            'label': label
        }
