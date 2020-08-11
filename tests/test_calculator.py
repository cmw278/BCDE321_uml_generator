from unittest import TestCase
from example import Calculator


class TestCalculator(TestCase):

    def test_add_one(self):
        expected = 1
        actual = Calculator.add(1)
        self.assertEqual(actual, expected)

    def test_add_one_and_three(self):
        expected = 4
        actual = Calculator.add(1, 3)
        self.assertEqual(actual, expected)
