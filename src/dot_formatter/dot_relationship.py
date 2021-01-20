from dot_formatter import DotObject, AssociationStrategy


class DotRelationship(DotObject):

    def __init__(self, source_class: str, target_class: str, label: str = ''):
        self.source_class = source_class
        self.target_class = target_class
        self.label = label
        self.strategy = None

    def assign_strategy(self, strategy: AssociationStrategy) -> None:
        self.strategy = strategy

    def __str__(self) -> str:
        if self.strategy is not None:
            return self.strategy.compose_string(
                self.source_class,
                self.target_class,
                self.label
            )
        else:
            return '%s -> %s [\n\n]' % (
                self.target_class,
                self.source_class
            )
