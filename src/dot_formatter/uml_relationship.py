from enum import Enum
from dot_formatter import (DotRelationship,
                           AssociationStrategy as Association,
                           InheritanceStrategy as Inheritance,
                           AggregationStrategy as Aggregation,
                           CompositionStrategy as Composition)


class UMLRelationship(Enum):
    """Enumerator to simplify the generation of UML relationship mark-up.
    The controller will interact directly with one of these enum values,
    passing it as an argument when defining a relationship. The receiver
    can then instantiate the appropriate DotRelationship class by calling
    UMLRelationship.make() with the required arguments.
    """

    ASSOCIATION = Association
    INHERITANCE = Inheritance
    AGGREGATION = Aggregation
    COMPOSITION = Composition

    def make(self, source_class: str, target_class: str,
             label: str) -> DotRelationship:
        relationship = DotRelationship(source_class, target_class, label)
        relationship.assign_strategy(self.value())
        return relationship
