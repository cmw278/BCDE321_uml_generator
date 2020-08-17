from unittest import TestCase
from dot_formatter import DotAssociation

# Test data dictionary
from test_data import DATA
_RELATIONSHIP = DATA['relationship']['association']
_CLASS_NAME = DATA['class_name']


class TestDotAssociation(TestCase):

    def setUp(self):
        self.relationship = DotAssociation(
            _CLASS_NAME,
            _RELATIONSHIP['target_class']
        )

    def test_attribute_my_class(self):
        expected = _CLASS_NAME
        actual = self.relationship.my_class
        self.assertEqual(actual, expected)

    def test_relationship_target_class(self):
        expected = _RELATIONSHIP['target_class']
        actual = self.relationship.target_class
        self.assertEqual(actual, expected)

    def test_relationship_label(self):
        expected = ''
        actual = self.relationship.label
        self.assertEqual(actual, expected)

    def test_to_string(self):
        expected = ('\n' + _RELATIONSHIP['target_class'] + ' -> '
                    + _CLASS_NAME)
        actual = str(self.relationship)
        self.assertEqual(actual, expected)
