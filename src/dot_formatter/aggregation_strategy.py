from dot_formatter import RelationshipStrategy


class AggregationStrategy(RelationshipStrategy):
    def compose_string(self, source_class: str,
                       target_class: str, label: str) -> str:
        return ('%s -> %s' % (source_class, target_class)
                + ' [\nlabel="%s"\narrowtail="ediamond"\n]' % label)
