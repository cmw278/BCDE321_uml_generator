from unittest import TestCase
from dot_formatter import (DotClass, DotObject, DotAttribute,
                           DotMethod, DotAssociation)

# Test data dictionary
from test_data import DATA
_METHOD = DATA['method']
_ATTRIBUTE = DATA['attribute']
_RELATIONSHIP = DATA['relationship']['association']
_CLASS_NAME = DATA['class_name']


class TestDotClass(TestCase):

    def setUp(self):
        # TODO: Implement DotClass
        self.skipTest('Awaiting implementation of DotClass')
        self.class_ = DotClass(_CLASS_NAME)

    def test_inheritance(self):
        expected = DotObject
        actual = self.class_
        self.assertIsInstance(expected, actual)

    def test_class__name(self):
        expected = _CLASS_NAME
        actual = self.class_.name
        self.assertEqual(actual, expected)

    def add_attribute(self):
        return self.class_.add_attribute(
            _ATTRIBUTE['name'],
            _ATTRIBUTE['type']
        )

    def test_add_attribute(self):
        expected = DotAttribute(_ATTRIBUTE['name'], _ATTRIBUTE['type'])
        actual = self.add_attribute()
        self.assertEqual(actual, expected)

    def add_method(self):
        return self.class_.add_method(
            _METHOD['name'],
            _METHOD['return_type']
        )

    def test_add_method(self):
        expected = DotMethod(_METHOD['name'], _METHOD['return_type'])
        actual = self.add_method()
        self.assertEqual(actual, expected)

    def add_relationship(self):
        return self.class_.add_relationship(
            _RELATIONSHIP['type'],
            _RELATIONSHIP['target_class']
        )

    def test_add_relationship(self):
        expected = DotRelationship(
            _CLASS_NAME,
            _RELATIONSHIP['target_class']
        )
        actual = self.add_relationship()
        self.assertEqual(actual, expected)

    def test_to_string(self):
        attribute = self.add_attribute()
        method = self.add_method()
        relationship = self.add_relationship()
        expected = ('<{<B>\\N</B>'
                    + '|' + str(attribute)
                    + '|' + str(method) + '}>'
                    + '\n' + str(relationship))
        actual = str(self.class_)
        self.assertEqual(actual, expected)
