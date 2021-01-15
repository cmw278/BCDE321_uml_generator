from unittest import TestCase
from unittest.mock import patch, Mock
from dot_formatter import DotObject


class TestDotAggregation(TestCase):

    @patch.multiple(
        DotObject,
        __abstractmethods__=set(),
        __str__=Mock(return_value='mocked')
    )
    def setUp(self):
        self.object = DotObject('Mock')

    def test_str(self):
        actual = self.object.__str__()
        self.assertIsNone(actual)

    def test_hash(self):
        test_set = set()
        for i in range(10):
            test_set.add(self.object)
        expected = 1
        actual = len(test_set)
        self.assertEqual(expected, actual)
