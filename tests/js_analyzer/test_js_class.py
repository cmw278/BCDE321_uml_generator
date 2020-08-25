from unittest import TestCase
from js_analyzer import JsClass
from js_analyzer_test_data import TOYBOX_CLASS, TOYBOX_DICT


class TestJsClass(TestCase):

    def setUp(self):
        self.class_ = JsClass(TOYBOX_CLASS)

    def test_js_class_name(self):
        """Class has a name"""
        expected = 'Toybox'
        actual = self.class_.name
        self.assertEqual(actual, expected)

    def test_js_class_has_four_methods(self):
        expected = 4
        actual = len(self.class_.methods)
        self.assertEqual(actual, expected)

    def test_js_class_has_one_attribute(self):
        expected = 1
        actual = len(self.class_.attributes)
        self.assertEqual(actual, expected)

    def test_js_class_to_dict(self):
        """Correctly presents as a dict"""
        expected = TOYBOX_DICT
        actual = self.class_.to_dict()
        self.assertEqual(actual, expected)
