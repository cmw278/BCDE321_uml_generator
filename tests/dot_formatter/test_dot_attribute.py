from unittest import TestCase
from dot_formatter import DotAttribute, DotArgument

# Test data dictionary
from test_data import DATA


class TestDotAttribute(TestCase):

    def setUp(self):
        # TODO: Implement DotAttribute
        self.skipTest('Awaiting implementation of DotAttribute')
        name = DATA['attribute']['name']
        type_ = DATA['attribute']['type']
        self.test_data = {
            'name': name,
            'type': type_
        }
        self.attribute = DotAttribute(name, type_)

    def test_inheritance(self):
        expected = DotArgument
        actual = self.attribute
        self.assertIsInstance(actual, expected)

    def test_attribute_name(self):
        expected = self.test_data['name']
        actual = self.attribute.name
        self.assertEqual(actual, expected)

    def test_attribute_type(self):
        expected = self.test_data['type']
        actual = self.attribute.type
        self.assertEqual(actual, expected)

    def test_to_string(self):
        expected = ('+ %s: %s<br/>'
                    % (self.test_data['name'], self.test_data['type']))
        actual = str(self.attribute)
        self.assertEqual(actual, expected)
