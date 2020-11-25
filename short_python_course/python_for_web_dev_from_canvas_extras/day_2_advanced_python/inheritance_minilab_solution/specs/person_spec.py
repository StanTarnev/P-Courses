import unittest
import sys
sys.path.append('.')
sys.path.append('..')
from person import *

class TestPerson(unittest.TestCase):

  def setUp(self):
    self.person = Person("Jack", "Jarvis")

  def test_person_has_first_name(self):
    self.assertEqual("Jack", self.person.get_first_name())

  def test_person_has_last_name(self):
    self.assertEqual("Jarvis", self.person.get_last_name())

  def test_person_can_talk(self):
    self.assertEqual("My name is Jack Jarvis", self.person.talk())

if __name__ == '__main__':
  unittest.main()