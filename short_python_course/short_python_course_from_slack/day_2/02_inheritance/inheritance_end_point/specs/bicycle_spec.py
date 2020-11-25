import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from bicycle import *

class TestBicycle(unittest.TestCase):
  def setUp(self):
    self.bicycle = Bicycle()

  def test_bicycle_has_2_wheels(self):
    self.assertEqual(2, self.bicycle.get_number_of_wheels())

if __name__ == "__main__":
    unittest.main()
