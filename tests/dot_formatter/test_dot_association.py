from unittest import TestCase
from dot_formatter import UMLRelationship

# Test data dictionary
from test_data import DATA


class TestDotAssociation(TestCase):

    def setUp(self):
        source_class = DATA['relationship']['source_class']
        target_class = DATA['relationship']['target_class']
        self.test_data = {
            'options': {
                'label': ''
            },
            'source_class': source_class,
            'target_class': target_class
        }
        self.relationship = UMLRelationship.ASSOCIATION.make(
            source_class,
            target_class,
            ''
        )

    def test_attribute_source_class(self):
        expected = self.test_data['source_class']
        actual = self.relationship.source_class
        self.assertEqual(actual, expected)

    def test_relationship_target_class(self):
        expected = self.test_data['target_class']
        actual = self.relationship.target_class
        self.assertEqual(actual, expected)

    def test_to_string(self):
        expected = ('%s -> %s [\nlabel=""\n]'
                    % (
                        self.test_data['target_class'],
                        self.test_data['source_class']
                    ))
        actual = str(self.relationship)
        self.assertEqual(actual, expected)
