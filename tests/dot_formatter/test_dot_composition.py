from unittest import TestCase
from dot_formatter import DotComposition
from test_dot_association import TestDotAssociation

# Test data dictionary
from test_data import DATA
_RELATIONSHIP = DATA['relationship']['composition']
_CLASS_NAME = DATA['class_name']


class TestDotComposition(TestDotAssociation):

    def setUp(self):
        # TODO: Implement DotComposition
        self.skipTest('Awaiting implementation of DotComposition')
        self.relationship = DotComposition(
            _CLASS_NAME,
            _RELATIONSHIP['target_class'],
            _RELATIONSHIP['label']
        )

    def test_relationship_label(self):
        expected = _RELATIONSHIP['label']
        actual = self.relationship.label
        self.assertEqual(actual, expected)

    def test_to_string(self):
        expected = ('\n%s -> %s [\narrowtail=diamond\nlabel="%s"\n]'
                    % (_CLASS_NAME, _RELATIONSHIP['target_class'],
                        _RELATIONSHIP['label']))
        actual = str(self.relationship)
        self.assertEqual(actual, expected)
