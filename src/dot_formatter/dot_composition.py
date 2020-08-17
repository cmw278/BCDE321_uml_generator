from dot_formatter import DotAggregation


class DotComposition(DotAggregation):

    def _set_options(self, label: str, arrowtail: str = 'diamond') -> None:
        # Override so that arrowtail defaults to `diamond` (filled diamond)
        # for composition relationship.
        return super()._set_options(label, arrowtail)
