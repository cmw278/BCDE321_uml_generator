from dot_formatter import (ClassBuilder, ClassDirector,
                           UMLRelationship, DotRelationship)
from pkg_resources import resource_filename
import gc


class DotFormatter:
    """Takes a dictionary representation of a software system and converts it
    to the string representation of a DOT file (Graphviz format)."""

    def __init__(self, system_dict: dict, *, template_path: str = None):
        """Optional keyword arguments:

        template_path (str): It is unlikely you will ever need to, but if
        you like you may provide a path to a template .gv (DOT) file to use
        for formatting the output. If no value is provided the system
        default is used."""

        self.name = None
        self.all_my_classes = []
        self.all_my_relationships = []
        assert ('template' not in system_dict,
                """'template' is a reserved key and may not be used in
                 user-defined dictionaries""")
        system_dict['template'] = template_path
        for key, setter in self._get_key_setter(self.__class__):
            if key in system_dict:
                setter(system_dict[key])
        assert self.name is not None, 'A girl must have a name'

    def _get_key_setter(self, component: object):
        """Generator used to provide mapping to system keys and
        their relevant setter methods. User defined translations
        may be provided in future to allow custom dictionary mappings
        to be used to represent a software system"""
        if component is self.__class__:
            # keys and setter methods for DotFormatter parameters
            yield 'folder_name', self._set_name
            yield 'classes', self._set_classes
            yield 'relationships', self._set_relationships
            yield 'template', self._set_template_file_path
        if component is DotRelationship:
            # keys for DotRelationship parameters
            yield 'source_class', None
            yield 'target_class', None
            yield 'type', None
            yield 'label', None

    def _set_name(self, name: str):
        self.name = name

    def _set_classes(self, classes: list) -> None:
        builder = ClassBuilder()
        director = ClassDirector(builder)
        for class_ in classes:
            director.make_class(class_)
            self.all_my_classes.append(builder.get_class())

    def _set_relationships(self, relationships: list) -> None:
        self.all_my_relationships = [self._get_relationship(relationship_dict)
                                     for relationship_dict in relationships]

    def _get_relationship(self, relationship_dict: dict) -> DotRelationship:
        keys = [key for key, setter in self._get_key_setter(DotRelationship)]
        source_class, target_class, relationship_type, label = (
            relationship_dict[key] if key in relationship_dict
            else None for key in keys
        )
        assert (source_class is not None and target_class is not None,
                'Source and target classes must be provided')
        try:
            return UMLRelationship[relationship_type].make(
                source_class,
                target_class,
                label
            )
        except KeyError:
            # If relationship_type is invalid, default to association
            # relationship
            return UMLRelationship['ASSOCIATION'].make(
                source_class,
                target_class,
                label
            )

    def _set_template_file_path(self, template_file_path):
        if template_file_path is None:
            self.template_file_path = (
                resource_filename(__name__, 'data/.gv.template')
            )
        else:
            self.template_file_path = template_file_path

    def __str__(self) -> str:
        template_file = open(self.template_file_path)
        template_string = template_file.read()
        template_file.close()
        del template_file
        gc.collect
        members = [
            '\n'.join([str(class_)
                       for class_ in self.all_my_classes]),
            '\n'.join([str(relationship)
                       for relationship in self.all_my_relationships])
        ]
        return template_string % (self.name, '\n'.join(members))
