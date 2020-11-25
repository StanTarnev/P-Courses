import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink_1 = Drink("beer", 2.00)
        self.drink_2 = Drink("wine", 3.00)
        self.drink_3 = Drink("gin", 4.00)
        self.pub = Pub("The Prancing Pony", 100.00)
        self.customer = Customer("Frodo", 10.00)
        
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    
    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)
        
    
    def test_pub_can_add_drinks(self):
        self.pub.add_drink(self.drink_1)
        self.assertEqual(1, self.pub.drink_count())
    
    
    def test_pub_cannot_serve_drink(self):
        self.pub.add_drink(self.drink_1)
        self.pub.add_drink(self.drink_2)
        self.pub.serve(self.customer, self.drink_1)
        self.assertEqual(8.00, self.customer.wallet)
        self.assertEqual(102.00, self.pub.till)
        self.assertEqual(1, self.pub.drink_count())
    
    
    def test_pub_cannot_serve_unstocked_drink(self):
        self.pub.add_drink(self.drink_1)
        self.pub.serve(self.customer, self.drink_2)
        self.assertEqual(10.00, self.customer.wallet)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(1, self.pub.drink_count())
    
    
    def test_pub_does_not_serve_too_many_drinks(self):
        self.pub.add_drink(self.drink_1)
        self.pub.add_drink(self.drink_1)
        self.pub.serve(self.customer, self.drink_1)
        self.assertEqual(1, self.pub.drink_count())
    
    
        