import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from vehicle import *

class TestVehicle(unittest.TestCase):
  def setUp(self):
    self.vehicle = Vehicle(4)

  def test_start_engine(self):
    self.assertEqual("Vrrmm", self.vehicle.start_engine())

  def test_vehicle_has_number_of_wheels(self):
    self.assertEqual(4, self.vehicle.get_number_of_wheels())

if __name__ == "__main__":
    unittest.main()
