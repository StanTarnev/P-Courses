import unittest
import sys
sys.path.append('.')
sys.path.append('..')
from medic import *

class TestMedic(unittest.TestCase):

  def setUp(self):
    self.medic = Medic("Victor", "McDade")

  def test_medic_has_first_name(self):
    self.assertEqual("Victor", self.medic.get_first_name())

  def test_medic_has_last_name(self):
    self.assertEqual("McDade", self.medic.get_last_name())

  def test_medic_can_talk(self):
    self.assertEqual("My name is Victor McDade", self.medic.talk())

  def test_medic_can_heal(self):
    self.assertEqual("I can heal people", self.medic.heal())

if __name__ == '__main__':
  unittest.main()