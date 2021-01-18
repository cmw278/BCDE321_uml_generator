from dot_formatter import RelationshipStrategy


class InheritanceStrategy(RelationshipStrategy):
    def compose_string(self, source_class: str,
                       target_class: str, label: str) -> str:
        return ('%s -> %s' % (target_class, source_class)
                + ' [\nlabel="%s"\narrowtail="empty"\n]' % label)
