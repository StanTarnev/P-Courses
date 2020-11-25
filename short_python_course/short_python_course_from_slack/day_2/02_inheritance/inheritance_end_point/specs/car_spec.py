import unittest
import sys
sys.path.append('.')
sys.path.append('..')
from car import *

class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car("Ferarri")

    def test_car_can_start_engine(self):
        self.assertEqual("Vrrmm", self.car.start_engine())

    def test_car_has_4_wheels(self):
        self.assertEqual(4, self.car.get_number_of_wheels())

    def test_car_has_model(self):
        self.assertEqual("Ferarri", self.car.get_model())

if (__name__) == "__main__":
    unittest.main()
