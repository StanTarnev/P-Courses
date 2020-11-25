import unittest
import sys
sys.path.append(".")
sys.path.append("..")

from Cake import *
from CakeShop import *

class CakeShopTest(unittest.TestCase):
    def setUp(self):
        ingredients1 = ["chocolate", "cocoa powder", "flour", "eggs", "sugar", "butter"]
        cake1 = Cake("Brownie", ingredients1, 5)

        ingredients2 = ["carrots", "raisins", "cinnamon", "flour", "eggs", "sugar", "butter"]
        cake2 = Cake("Carrot Cake", ingredients2, 2.5)

        ingredients3 = ["lemon juice", "flour", "eggs", "sugar", "butter"]
        cake3 = Cake("Lemon Drizzle", ingredients3, 1.5)

        cakes = [cake1, cake2, cake3]
        self.cake_shop = CakeShop(cakes)

    def test_average_cake_rating(self):
        self.assertEqual(self.cake_shop.get_average_rating(), 3)

if __name__ == '__main__':
    unittest.main()
