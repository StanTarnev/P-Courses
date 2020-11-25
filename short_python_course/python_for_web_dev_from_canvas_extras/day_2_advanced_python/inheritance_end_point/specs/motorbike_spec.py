import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from motorbike import *

class TestMotorbike(unittest.TestCase):
  def setUp(self):
    self.motorbike = MotorBike()

  def test_motorbike_can_start_engine(self):
    self.assertEqual("Vrrmm (I'm a motorbike), HELL YEAH!", self.motorbike.start_engine())

  def test_motorbike_has_2_wheels(self):
    self.assertEqual(2, self.motorbike.get_number_of_wheels())

if __name__ == "__main__":
    unittest.main()
