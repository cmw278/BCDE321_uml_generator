from unittest import TestCase
from dot_formatter import DotAggregation
from test_dot_association import TestDotAssociation

# Test data dictionary
from test_data import DATA
_RELATIONSHIP = DATA['relationship']['aggregation']
_CLASS_NAME = DATA['class_name']


class TestDotAggregation(TestDotAssociation):

    def setUp(self):
        # TODO: Implement DotAggregation
        self.skipTest("Awaiting implementation of DotAggregation")
        self.relationship = DotAggregation(
            _CLASS_NAME,
            _RELATIONSHIP['target_class'],
            _RELATIONSHIP['label']
        )

    def test_relationship_label(self):
        expected = _RELATIONSHIP['label']
        actual = self.relationship.label
        self.assertEqual(actual, expected)

    def test_to_string(self):
        expected = (_RELATIONSHIP['target_class'] + ' -> ' + _CLASS_NAME
                    + ' [\n'
                    + 'arrowtail=empty\n'
                    + 'label="' + _RELATIONSHIP['label'] + '"\n'
                    + ']')
        actual = str(self.relationship)
        self.assertEqual(actual, expected)
