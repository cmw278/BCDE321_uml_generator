from unittest import TestCase
from js_analyzer import JsIdentifier
from js_analyzer_test_data import NEWNAME_IDENTIFIER


class TestJsIdentifier(TestCase):

    def setUp(self):
        self.identifier = JsIdentifier(NEWNAME_IDENTIFIER)

    def test_js_identifier_name(self):
        """Identifier has a name"""
        expected = 'newName'
        actual = self.identifier.name
        self.assertEqual(actual, expected)

    def test_js_identifier_type(self):
        """Type defaults to any"""
        expected = 'any'
        actual = self.identifier.type
        self.assertEqual(actual, expected)

    def test_js_identifier_to_dict(self):
        """Correctly presents as a dict"""
        expected = {
            'name': 'newName',
            'type': 'any'
        }
        actual = self.identifier.to_dict()
        self.assertEqual(actual, expected)

    def test_js_identifier_set_type(self):
        self.identifier.set_type('String')
        expected = {
            'name': 'newName',
            'type': 'String'
        }
        actual = self.identifier.to_dict()
        self.assertEqual(actual, expected)
