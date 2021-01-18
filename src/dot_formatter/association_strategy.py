from dot_formatter import RelationshipStrategy


class AssociationStrategy(RelationshipStrategy):
    def compose_string(self, source_class: str,
                       target_class: str, label: str) -> str:
        return ('%s -> %s' % (target_class, source_class)
                + ' [\nlabel="%s"\n]' % label)
