class Library:

  def __init__(self, books):
    self.books = books

  def get_books(self):
    return self.books

  def find_book(self,title):
    for book in self.books:
      if(book["title"] == title):
        return book
    return None

  def find_renting_info(self,title):
    info = "Book not found."
    book = self.find_book(title)
    if(book != None):
      info = book["rental_details"] 
    return info

  def add_book(self,new_book_title):
    new_book = {
      "title": new_book_title, 
      "rental_details": {
        "student_name": "", 
        "date": ""
        }
      }
    self.books.append(new_book)

  def rent_book(self, book_title, student, due_date):
    book = self.find_book(book_title)
    book["rental_details"] = { "student_name": student, "date": due_date }

