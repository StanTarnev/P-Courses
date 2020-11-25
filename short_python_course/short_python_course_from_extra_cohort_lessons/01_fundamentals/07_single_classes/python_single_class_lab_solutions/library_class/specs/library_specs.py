import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from library import *

class LibraryTest(unittest.TestCase):

  def setUp(self):

    books = [
      { 
        "title": "lord_of_the_rings",
        "rental_details": { 
          "student_name": "Jeff",
          "date": "01/12/2016"
        } 
      },
      { 
        "title": "colour_of_magic",
        "rental_details": {
          "student_name": "",
          "date": "" 
        }
      }
    ]

    self.library = Library(books)

  def test_list_books(self):
    book_list = self.library.get_books()
    self.assertEqual(self.library.get_books(), book_list)

  def test_find_book(self):
    found_book = self.library.find_book("colour_of_magic")
    self.assertEqual("colour_of_magic", found_book["title"])

  def test_find_book__book_not_in_library(self):
    found_book = self.library.find_book("harry_potter")
    self.assertIsNone(found_book)

  def test_check_who_is_renting(self):
    self.assertEqual({"student_name": "Jeff", "date": "01/12/2016"}, self.library.find_renting_info("lord_of_the_rings"))

  def test_can_add_book(self):
    self.library.add_book("1984")
    self.assertEqual({ "title": "1984", "rental_details": { "student_name": "", "date": ""} }, self.library.find_book("1984"))
    all_books = self.library.get_books()
    self.assertEqual(3, len(all_books))

  def test_can_rent_out_book(self):
    self.library.rent_book("colour_of_magic", "Paul", "05/12/2016")
    renting_info = self.library.find_renting_info("colour_of_magic")
    self.assertEqual({
      "student_name": "Paul",
      "date":"05/12/2016"
      } , renting_info)

if __name__ == "__main__":
    unittest.main()
