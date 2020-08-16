from unittest import TestCase
from dot_formatter import DotArgument, DotObject

# Test data dictionary
from test_data import DATA
_ARGUMENT = DATA['argument']


class TestDotArgument(TestCase):
    def setUp(self):
        # TODO: Implement DotArgument
        self.skipTest('Awaiting implementation of DotArgument')
        self.argument = DotArgument(_ARGUMENT['name'], _ARGUMENT['type'])

    def test_inheritance(self):
        expected = DotObject
        actual = self.argument
        self.assertIsInstance(expected, actual)

    def test_argument_name(self):
        expected = _ARGUMENT['name']
        actual = self.argument.name
        self.assertEqual(actual, expected)

    def test_argument_type(self):
        expected = _ARGUMENT['type']
        actual = self.argument.type
        self.assertEqual(actual, expected)

    def test_to_string(self):
        expected = _ARGUMENT['name'] + ': ' + _ARGUMENT['type']
        actual = str(self.argument)
        self.assertEqual(actual, expected)
