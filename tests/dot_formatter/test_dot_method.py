from unittest import TestCase
from dot_formatter import DotMethod, DotObject, DotArgument

# Test data dictionary
from test_data import DATA
_METHOD = DATA['method']
_ARGUMENT = DATA['argument']


class TestDotMethod(TestCase):

    def setUp(self):
        # TODO: Implement DotMethod
        self.skipTest('Awaiting implementation of DotMethod')
        self.method = DotMethod(_METHOD['name'], _METHOD['return_type'])

    def test_inheritance(self):
        expected = DotObject
        actual = self.method
        self.assertIsInstance(expected, actual)

    def test_method_name(self):
        expected = _METHOD['name']
        actual = self.method.name
        self.assertEqual(actual, expected)

    def test_method_return_type(self):
        expected = _METHOD['return_type']
        actual = self.method.type
        self.assertEqual(actual, expected)

    def test_add_argument(self):
        expected = DotArgument(_ARGUMENT['name'], _ARGUMENT['type'])
        actual = self.method.add_argument(argument_name, argument_type)
        self.assertEqual(expected, actual)

    def test_to_string(self):
        expected = ('+ ' + _ARGUMENT['name'] + '(): '
                         + _ARGUMENT['type'] + '<br/>')
        actual = str(self.method)
        self.assertEqual(actual, expected)
