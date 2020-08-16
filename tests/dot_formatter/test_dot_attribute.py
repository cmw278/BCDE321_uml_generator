from unittest import TestCase
from dot_formatter import DotAttribute, DotArgument

# Test data dictionary
from test_data import DATA
_ATTRIBUTE = DATA['attribute']


class TestDotAttribute(TestCase):

    def setUp(self):
        # TODO: Implement DotAttribute
        self.skipTest('Awaiting implementation of DotAttribute')
        self.attribute = DotAttribute(_ATTRIBUTE['name'], _ATTRIBUTE['type'])

    def test_inheritance(self):
        expected = DotArgument
        actual = self.attribute
        self.assertIsInstance(expected, actual)

    def test_attribute_name(self):
        expected = _ATTRIBUTE['name']
        actual = self.attribute.name
        self.assertEqual(actual, expected)

    def test_attribute_type(self):
        expected = _ATTRIBUTE['type']
        actual = self.attribute.type
        self.assertEqual(actual, expected)

    def test_to_string(self):
        expected = ('+ ' + _ATTRIBUTE['name'] + ': '
                         + _ATTRIBUTE['type'] + '<br/>')
        actual = str(self.attribute)
        self.assertEqual(actual, expected)
