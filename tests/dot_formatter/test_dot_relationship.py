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

    def test_str(self):
        actual = self.relationship._set_options('label')
        self.assertIsNone(actual)
