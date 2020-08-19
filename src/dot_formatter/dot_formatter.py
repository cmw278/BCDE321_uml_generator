from dot_formatter import (DotClass, DotAttribute, DotMethod, DotArgument,
                           UMLRelationship, DotRelationship)


class DotFormatter:
    """Takes a dictionary representation of a software system and converts it
    to the string representation of a DOT file (Graphviz format)."""

    def __init__(self, system_dict: dict):
        self.name = None
        self.all_my_classes = []
        self.all_my_relationships = []
        for key, setter in self._get_key_setter(self.__class__):
            setter(system_dict[key]) if key in system_dict else None
        assert self.name is not None, 'A girl must have a name'

    def _get_key_setter(self, component: object):
        """Point for expansion:
        User-defined dictionary keys may be provided to this system.
        User-defined keys could be read from a json file, or possibly
        some other format."""
        if component is self.__class__:
            yield 'folder_name', self._set_name
            yield 'classes', self._set_classes
            yield 'relationships', self._set_relationships
        if component is DotClass:
            yield 'attributes', self._populate_class_attributes
            yield 'methods', self._populate_class_methods
        if component is DotAttribute:
            yield 'name', None
            yield 'type', None
        if component is DotMethod:
            # TODO: Finish this thought
            pass
        if component is DotArgument:
            pass

    def _set_name(self, name: str):
        self.name = name

    def _set_classes(self, classes: list) -> None:
        self.all_my_classes = [self._get_class(class_dict)
                               for class_dict in classes]

    def _get_class(self, class_dict: dict) -> DotClass:
        new_class = DotClass(class_dict['name'])
        for key, setter in self._get_key_setter(DotClass):
            setter(new_class, class_dict[key]) if key in class_dict else None
        return new_class

    def _populate_class_attributes(
            self,
            class_: DotClass,
            attributes: list) -> None:
        name, type_ = (
            key for key, setter in self._get_key_setter(DotAttribute))
        # Add typeless attributes first
        [class_.add_attribute(attribute[name])
         for attribute in attributes if type_ not in attribute]
        # Add typed attributes last
        [class_.add_attribute(attribute[name], attribute[type_])
         for attribute in attributes if type_ in attribute]

    def _populate_class_methods(self, class_: DotClass, methods: list) -> None:
        # TODO: _populate_class_methods
        # Should be similar to _populate_class_attributes
        pass

    def _set_relationships(self, relationships: list) -> None:
        self.all_my_relationships = [self._get_relationship(relationship_dict)
                                     for relationship_dict in relationships]

    def _get_relationship(self, relationship_dict: dict) -> DotRelationship:
        # TODO: _get_relationship
        pass

    def __str__(self) -> str:
        # TODO: Finish this thought
        return '\n'.join([str(class_) for class_ in self.all_my_classes])
