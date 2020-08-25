from unittest import TestCase
from js_analyzer import JsMethod
from js_analyzer_test_data import ADDTOY_METHOD, ADDTOY_DICT


class TestJsMethod(TestCase):

    def setUp(self):
        self.method = JsMethod(ADDTOY_METHOD)

    def test_js_method_name(self):
        """Method has a name"""
        expected = 'addToy'
        actual = self.method.name
        self.assertEqual(actual, expected)

    def test_js_method_has_three_arguments(self):
        expected = 3
        actual = len(self.method.arguments)
        self.assertEqual(actual, expected)

    def test_js_method_to_dict(self):
        """Correctly presents as a dict"""
        expected = ADDTOY_DICT
        actual = self.method.to_dict()
        self.assertEqual(actual, expected)
