from dot_formatter import (DotObject, DotAttribute, DotMethod,
                           DotRelationship, UMLRelationship)


class DotClass(DotObject):

    def __init__(self, name):
        super().__init__(name)
        self.all_my_attributes = []
        self.all_my_methods = []
        self.all_my_relationships = []

    def add_attribute(self, attribute_name: str,
                      attribute_type: str) -> DotAttribute:
        new_attribute = DotAttribute(attribute_name, attribute_type)
        self.all_my_attributes.append(new_attribute)
        return new_attribute

    def add_method(self, method_name: str,
                   method_return_type: str) -> DotMethod:
        new_method = DotMethod(method_name, method_return_type)
        self.all_my_methods.append(new_method)
        return new_method

    def add_relationship(self, relationship_type: UMLRelationship,
                         target_class: str,
                         label: str = '') -> DotRelationship:
        """relationship_type is an Enum instance that references
        DotRelationship subclasses. relationship_type.make(*args)
        instantiates the relevant class using the default constructor."""
        new_relationship = (relationship_type
                            .make(self.name, target_class, label))
        self.all_my_relationships.append(new_relationship)
        return new_relationship

    def __str__(self):
        return ('%s [\nlabel="{\\N|%s|%s}"\n]\n%s'
                % (
                    self.name,
                    ''.join([str(an_attribute) for an_attribute
                             in self.all_my_attributes]),
                    ''.join([str(a_method) for a_method
                             in self.all_my_methods]),
                    '\n'.join([str(a_relationship) for a_relationship
                               in self.all_my_relationships])
                ))
