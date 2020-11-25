import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from student import *

class StudentTest(unittest.TestCase):

  def setUp(self):

    self.student = Student("Jeff", 6)

  def test_student_has_name(self):
    self.assertEqual("Jeff", self.student.get_name())

  def test_student_has_cohort(self):
    self.assertEqual(6, self.student.get_cohort())
  
  def test_students_name_can_update(self):
    self.student.set_name("Paul")
    self.assertEqual("Paul", self.student.get_name())

  def test_student_can_change_cohort(self):
    self.student.set_cohort(9)
    self.assertEqual(9, self.student.get_cohort())

  def test_student_can_talk(self):
    self.assertEqual("I can talk", self.student.talk())

  def test_student_has_favourite_language(self):
    self.assertEqual("I love Python", self.student.say_favourite_language("Python"))

if __name__ == "__main__":
  unittest.main()
