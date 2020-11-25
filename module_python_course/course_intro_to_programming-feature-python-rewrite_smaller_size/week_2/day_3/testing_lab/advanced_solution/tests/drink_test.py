import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("wine", 4.00, 5)
        
    
    def test_drink_has_name(self):
        self.assertEqual("wine", self.drink.name)
                        
                        
    def test_drink_has_price(self):
        self.assertEqual(4.00, self.drink.price) 
        
    
    def test_drink_has_alcohol_level(self):
        self.assertEqual(5, self.drink.alcohol_level)             
