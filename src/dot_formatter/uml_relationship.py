from enum import Enum
from dot_formatter import (DotAssociation, DotInheritance, DotAggregation,
                           DotRelationship, DotComposition)


class UMLRelationship(Enum):
    """Enumerator to simplify the generation of UML relationship mark-up.
    The controller will interact directly with one of these enum values,
    passing it as an argument when defining a relationship. The receiver
    can then instantiate the appropriate DotRelationship class by calling
    UMLRelationship.make() with the required arguments.
    """

    ASSOCIATION = DotAssociation
    INHERITANCE = DotInheritance
    AGGREGATION = DotAggregation
    COMPOSITION = DotComposition

    def make(self, source_class: str, target_class: str,
             label: str) -> DotRelationship:
        return self.value(source_class, target_class, label)
