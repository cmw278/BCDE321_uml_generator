class AssociationStrategy:
    @staticmethod
    def compose_string(source_class: str,
                       target_class: str, label: str) -> str:
        return ('%s -> %s' % (target_class, source_class)
                + ' [\nlabel="%s"\n]' % label)
