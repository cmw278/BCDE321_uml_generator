class CompositionStrategy:
    @staticmethod
    def compose_string(source_class: str,
                       target_class: str, label: str) -> str:
        return ('%s -> %s' % (source_class, target_class)
                + ' [\nlabel="%s"\narrowtail="diamond"\n]' % label)
