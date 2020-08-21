from dot_formatter import DotInheritance


class DotAggregation(DotInheritance):

    def __init__(self, source_class: str, target_class: str, label: str = ''):
        # Invert source and target for aggregation relationship.
        # i.e. Source contains target, so __str__() output is like:
        # `source -> target`.
        super().__init__(target_class, source_class, label)

    def _set_options(self, label: str, arrowtail: str = 'ediamond') -> None:
        # Override so that arrowtail defaults to `ediamond` (empty diamond)
        # for composition relationship.
        return super()._set_options(label, arrowtail)
