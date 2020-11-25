import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_max_3_1_returns_3(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))


    def test_max_3_5_returns_3_is_less_than_5(self):
        self.assertEqual("3 is less than 5", compare(3, 5))


    def test_max_10_10_returns_both_numbers_are_equal(self):
        self.assertEqual("both numbers are equal", compare(10, 10))
