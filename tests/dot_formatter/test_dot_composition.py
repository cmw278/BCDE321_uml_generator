from unittest import TestCase
from dot_formatter import UMLRelationship
from test_dot_inheritance import TestDotInheritance

# Test data dictionary
from test_data import DATA


class TestDotComposition(TestDotInheritance):

    def setUp(self):
        source_class = DATA['relationship']['source_class']
        target_class = DATA['relationship']['target_class']
        label = DATA['relationship']['label']
        self.test_data = {
            'options': {
                'label': label,
                'arrowtail': 'diamond'
            },
            'source_class': target_class,
            'target_class': source_class,
        }
        self.relationship = UMLRelationship.COMPOSITION.make(
            source_class,
            target_class,
            label
        )
