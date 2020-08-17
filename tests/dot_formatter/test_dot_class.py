from unittest import TestCase
from dot_formatter import (DotClass, DotObject, DotAttribute,
                           DotMethod, DotAssociation)

# Test data dictionary
from test_data import DATA


class TestDotClass(TestCase):

    def setUp(self):
        # TODO: Implement DotClass
        self.skipTest('Awaiting implementation of DotClass')
        class_name = DATA['class_name']
        method = DATA['method']
        attribute = DATA['attribute']
        target_class = DATA['relationship']['target_class']
        self.test_data = {
            'class_name': class_name,
            'method': method,
            'attribute': attribute,
            'target_class': target_class
        }
        self.class_ = DotClass(class_name)

    def test_inheritance(self):
        expected = DotObject
        actual = self.class_
        self.assertIsInstance(expected, actual)

    def test_class__name(self):
        expected = test_data['class_name']
        actual = self.class_.name
        self.assertEqual(actual, expected)

    def add_attribute(self):
        return self.class_.add_attribute(
            self.test_data['attribute']['name'],
            self.test_data['attribute']['type']
        )

    def test_add_attribute(self):
        name = self.test_data['attribute']['name']
        type_ = self.test_data['attribute']['type']
        expected = DotAttribute(name, type_)
        actual = self.add_attribute()
        self.assertEqual(actual, expected)

    def add_method(self):
        return self.class_.add_method(
            self.test_data['method']['name'],
            self.test_data['method']['return_type']
        )

    def test_add_method(self):
        name = self.test_data['method']['name']
        type_ = self.test_data['method']['type']
        expected = DotMethod(name, type_)
        actual = self.add_method()
        self.assertEqual(actual, expected)

    def add_relationship(self):
        return self.class_.add_relationship(
            self.test_data['target_class']
        )

    def test_add_relationship(self):
        expected = DotRelationship(
            self.test_data['class_name'],
            self.test_data['target_class']
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
