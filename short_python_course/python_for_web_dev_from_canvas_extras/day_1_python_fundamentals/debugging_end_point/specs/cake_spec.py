import unittest
import sys
sys.path.append(".")
sys.path.append("..")

from Cake import *

class TestCake(unittest.TestCase):
    def setUp(self):
        ingredients1 = ["chocolate", "cocoa powder", "flour", "eggs", "sugar", "butter"]
        self.cake = Cake("Brownie", ingredients1, 5)

    def test_cake_has_name(self):
        self.assertEqual(self.cake.name, "Brownie")

    def test_cake_has_ingredients(self):
        self.assertEqual(6, len(self.cake.ingredients))

    def test_cake_has_rating(self):
        self.assertEqual(5, self.cake.rating)

if __name__ == '__main__':
    unittest.main()
