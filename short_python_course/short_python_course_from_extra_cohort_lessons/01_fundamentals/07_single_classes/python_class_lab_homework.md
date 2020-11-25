# Classes Lab / Homework

In this lab, we'd like you to make some classes of your own. Below we've outlined a few scenarios to be modelled as Classes. Throughout each part stick to using our Test Driven Development process of writing our tests first then writing our methods and refactoring until they pass.

## Learning Objectives

1. Create your own class
2. Create multiple objects
3. Add some properties
4. Add some methods and behaviours
5. Get methods and behaviours to interact with properties

### Part A

For this part we want you to make a class that represents a CodeClan student. 

* Create a Class called Student that takes in a name (String) and a cohort (integer) when an new instance is created.
* Create a couple of Getter methods, one that returns the name property and one that returns the cohort property of the student.
* Add in Setter methods to update the students name and what cohort they are in.
* Create a method that gets the student to talk (eg. Returns "I can talk!).
* Create a method that takes in a students favourite programming language and returns it as part of a string (eg. `student1.say_favourite_language("Python")` -> "I love Python").


### Part B

Now we would like you to make a class that represents a sports team.

* Make a class to represent a Team that has the properties Team name (String), Players (List of strings) and a Coach (String).
* For each property in the class make a Getter method than can return them.
* Create a setter method to allow the coach's name to be updated.
* Create a method that adds a new player to the player's list.
* Add a method that takes in a string of a player's name and checks to see if they are in the players list.
* Add a points property into your class that starts at 0.
* Create a method that takes in whether the team has won or lost and updates the points property for a win.

### Extension:

Model a Library as a class.

* Create a class for a Library that has an list of books. Each book should be a dictionary with a title, which is a string, and rental details, which is another dictionary with a student name and due date.  

This should look something like:

```python
  { 
    "title": "lord_of_the_rings",
    "rental_details": { 
     "student_name": "Jeff", 
     "date": "01/12/16"
    }
  }

```


* Create a method that list all the books and their corresponding details. 
* Create a method that takes in a book title and returns all of the information about that book.
* Create a method that takes in a book title and returns only the rental details for that book. 
* Create a method that takes in a book title and adds it to our book list (Add a new dictionary for the book with the student name and date being left as empty strings)
* Create a method that changes the rental details of a book by taking in the title of the book, the student renting it and the date it's due to be returned. 
