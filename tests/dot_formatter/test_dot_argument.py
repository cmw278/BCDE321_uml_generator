from unittest import TestCase
from dot_formatter import DotArgument, DotObject

# Test data dictionary
from test_data import DATA


class TestDotArgument(TestCase):
    def setUp(self):
        name = DATA['argument']['name']
        type_ = DATA['argument']['type']
        self.test_data = {
            'name': name,
            'type': type_
        }
        self.argument = DotArgument(name, type_)

    def test_inheritance(self):
        expected = DotObject
        actual = self.argument
        self.assertIsInstance(actual, expected)

    def test_argument_name(self):
        expected = self.test_data['name']
        actual = self.argument.name
        self.assertEqual(actual, expected)

    def test_argument_type(self):
        expected = self.test_data['type']
        actual = self.argument.type
        self.assertEqual(actual, expected)

    def test_to_string(self):
        expected = '%s: %s' % (self.test_data['name'], self.test_data['type'])
        actual = str(self.argument)
        self.assertEqual(actual, expected)
