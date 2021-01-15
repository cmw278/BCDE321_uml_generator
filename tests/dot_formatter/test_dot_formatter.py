from unittest import TestCase
from dot_formatter import (DotFormatter, UMLRelationship, DotClass,
                           DotAssociation)

# Test data dictionary
from test_data import TOYBOX_TOY, EXPECTED_OUTPUT


class TestDotFormatter(TestCase):

    def setUp(self):
        self.test_data = TOYBOX_TOY
        self.expected_output = EXPECTED_OUTPUT
        self.formatter = DotFormatter(self.test_data)

    def test_formatter_name(self):
        expected = self.test_data['folder_name']
        actual = self.formatter.name
        self.assertEqual(expected, actual)

    def test_two_classes(self):
        expected = len(self.test_data['classes'])
        actual = len(self.formatter.all_my_classes)
        self.assertEqual(expected, actual)

    def get_class_expected_actual(self, ref_index: int) -> (list, DotClass):
        expected_class_one = self.test_data['classes'][ref_index]
        actual_class_one = self.formatter.all_my_classes[ref_index]
        return expected_class_one, actual_class_one

    def count_attributes_expected_actual(self, ref_index: int) -> (int, int):
        expected_class, actual_class\
            = self.get_class_expected_actual(ref_index)
        return (
            len(expected_class['attributes']),
            len(actual_class.all_my_attributes)
        )

    def test_class_one_has_three_attributes(self):
        expected, actual = self.count_attributes_expected_actual(0)
        self.assertEqual(expected, actual)

    def test_class_two_has_one_attribute(self):
        expected, actual = self.count_attributes_expected_actual(1)
        self.assertEqual(expected, actual)

    def count_methods_expected_actual(self, ref_index: int) -> (int, int):
        expected_class, actual_class\
            = self.get_class_expected_actual(ref_index)
        return (
            len(expected_class['methods']),
            len(actual_class.all_my_methods)
        )

    def test_class_one_has_two_methods(self):
        expected, actual = self.count_methods_expected_actual(0)
        self.assertEqual(expected, actual)

    def test_class_two_has_four_methods(self):
        expected, actual = self.count_methods_expected_actual(1)
        self.assertEqual(expected, actual)

    def test_formatter_has_one_relationship(self):
        expected = len(self.test_data['relationships'])
        actual = len(self.formatter.all_my_relationships)
        self.assertEqual(expected, actual)

    def test_to_string(self):
        expected = self.expected_output
        actual = str(self.formatter)
        self.assertEqual(expected, actual)

    def test_default_relationship(self):
        expected_class = DotAssociation
        actual_instance = self.formatter._get_relationship({
            'source_class': 'source',
            'target_class': 'target'
        })
        self.assertIsInstance(actual_instance, expected_class)

    def test_template_path(self):
        expected = '/dev/null'
        self.formatter._set_template_file_path(expected)
        actual = self.formatter.template_file_path
        self.assertEqual(expected, actual)
