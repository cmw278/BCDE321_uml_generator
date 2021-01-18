from unittest import TestCase
from unittest.mock import patch, Mock
from dot_formatter import DotRelationship


class TestDotRelationship(TestCase):

    @patch.multiple(
        DotRelationship,
        __abstractmethods__=set()
    )
    def setUp(self):
        self.relationship = DotRelationship('source', 'target')
        self.relationship.options = dict()

    def test_str(self):
        expected = 'target -> source [\n\n]'
        actual = str(self.relationship)
        self.assertEqual(expected, actual)
