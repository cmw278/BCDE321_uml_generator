from unittest import TestCase
from dot_formatter import DotInheritance
from test_dot_association import TestDotAssociation

# Test data dictionary
from test_data import DATA
_RELATIONSHIP = DATA['relationship']['inheritance']
_CLASS_NAME = DATA['class_name']


class TestDotInheritance(TestDotAssociation):

    def setUp(self):
        # TODO: Implement DotInheritance
        self.skipTest("Awaiting implementation of DotInheritance")
        self.relationship = DotInheritance(
            _CLASS_NAME,
            _RELATIONSHIP['target_class']
        )

    def test_to_string(self):
        expected = (_RELATIONSHIP['target_class'] + ' -> ' + _CLASS_NAME
                    + ' [\n'
                    + 'arrowtail=empty\n'
                    + ']')
        actual = str(self.relationship)
        self.assertEqual(actual, expected)
