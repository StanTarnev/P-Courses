import unittest

from classes.car import Car
from classes.engine import Engine
from classes.gearbox import Gearbox

class TestCar(unittest.TestCase):

    def setUp(self):
        self.engine = Engine()
        self.gearbox = Gearbox("manual", 5)
        self.car = Car("Ford", "Escort", self.engine, self.gearbox)

    def test_car_can_start(self):
        self.assertEqual("Vrrrmmm!", self.car.start())

    def test_car_can_change_gear(self):
        self.car.change_gear(2)
        self.assertEqual(2, self.car.gearbox.current_gear)
