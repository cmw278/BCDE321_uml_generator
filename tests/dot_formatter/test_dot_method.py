from unittest import TestCase
from dot_formatter import DotMethod, DotObject, DotArgument

# Test data dictionary
from test_data import DATA


class TestDotMethod(TestCase):

    def setUp(self):
        # TODO: Implement DotMethod
        self.skipTest('Awaiting implementation of DotMethod')
        name = DATA['method']['name']
        return_type = DATA['method']['return_type']
        argument = DATA['argument']
        self.test_data = {
            'name': name,
            'return_type': return_type,
            'argument': argument
        }
        self.method = DotMethod(name, return_type)

    def test_inheritance(self):
        expected = DotObject
        actual = self.method
        self.assertIsInstance(actual, expected)

    def test_method_name(self):
        expected = self.test_data['name']
        actual = self.method.name
        self.assertEqual(actual, expected)

    def test_method_return_type(self):
        expected = self.test_data['return_type']
        actual = self.method.return_type
        self.assertEqual(actual, expected)

    def test_add_argument(self):
        argument_name = self.test_data['argument']['name']
        argument_type = self.test_data['argument']['type']
        expected = DotArgument(argument_name, argument_type)
        actual = self.method.add_argument(argument_name, argument_type)
        self.assertEqual(expected, actual)

    def test_to_string(self):
        name = self.test_data['name']
        return_type = self.test_data['return_type']
        expected = '+ %s(): %s\\l' % (name, return_type)
        actual = str(self.method)
        self.assertEqual(actual, expected)
