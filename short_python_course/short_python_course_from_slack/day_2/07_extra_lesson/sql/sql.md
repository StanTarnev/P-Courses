# Python and SQL

**Duration: 120 minutes**

## Learning Objectives

- Be able to set up a basic SQLite database
- Understand `connection` and `cursor`
- Be able to put together a basic command line app that uses a database together with objects

## Introduction

At the moment, when we run our programs, any data used by them is lost. We can use a database to solve this problem; to persist data in between runs of our program.

The database engine we'll be using is [SQLite](https://www.sqlite.org/). SQLite is the most widely-used database in the world - it is used extensively in every Android and iOS device, most televisions and automotive multimedia systems, and millions of other applications.

In fact, [it is estimated](https://www.sqlite.org/mostdeployed.html) that there are over a trillion SQLite databases in the world. Although it's hard to tell for sure, it is possible that SQLite is the most common software library in use today.

It uses an implementation of the language SQL, which we assume you will be familiar with already. Should you wish to use a different database engine, it should be a relatively trivial process to change over.

We don't need to do any additional configuration or installation to Python to use it - it comes included with Python3!

Let's get started.

> Create a new script in atom called data_handler.py

## Setting Up

As we noted before, SQLite is included in Python. To get started, we can simply import the library to work with:

```python
# data_handler.py

import sqlite3
```

Next, we should tell our script the location of the database:

```python
import sqlite3

# ADDED
connection = sqlite3.connect("./students.db")
```

We create a variable, `connection`, that will represent our connection to the database. To this we assign the return value of `sqlite3.connect("./students.db")`.

This takes a single actual parameter, which is a String containing the filepath to the database.

If a database exists at this path, Python will open a connection to it. If the database _doesn't_ exist, Python will create it for us.

Next, we're going to create a `cursor` object. Cursors represent sets of rows in our database, and allow traversal over these rows as required. They also allow us to execute SQL commands.

```python
import sqlite3

connection = sqlite3.connect("./students.db")

# ADDED
cursor = connection.cursor()
```

This is all the set up we need to do. We've imported the library, and created `connection` and `cursor` objects. We're ready to start programming!

## Creating our Database Structure

Let's say that we want to create a database to store student information. We'll keep it relatively simple for now; we're going to have a single table, `students`, which will store a student's `first_name`, `surname`, and `age`. Each student will also have a primary key, `id`.

Firstly, we have to decide what data type SQLite will use to store each column. SQLite has the following five types:

**NULL**: Represents an empty value <br />
**INTEGER**: Represents signed (+/-) whole number <br />
**REAL**: Represents a floating point value <br />
**TEXT**: Represents a text string <br />
**BLOB**: Represents a "blob" of data, exactly as it was input

So our `first_name` and `surname` columns will be of type `TEXT`, and our `age` column will be an integer.

This means that the resulting SQL for creating the table might look like this:

```sql
CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, surname TEXT, age INTEGER)
```

Let's write a function that executes this SQL on our database!

```python
def set_up_table():
    cursor.execute("DROP TABLE IF EXISTS students")
    cursor.execute("""
      CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        surname TEXT,
        age INTEGER
      )
    """)
    connection.commit()
```

Note that we're using Python's multi-line strings here, delimited with `"""` at the start and end. For the sake of demonstration, we're also wiping the database table each time the program runs. **Of course, we wouldn't do this if this was a real application.**

Great! We use our cursor to execute the SQL, then call `connection.commit()` to confirm our change to the database. SQLite is a _transactional_ database; that is, we can make multiple changes to our database before confirming them with `commit`. This means that if one SQL command fails, all of our commands will fail. This helps to ensure consistency of data.

Let's continue. We're certainly going to need a function to insert a student. It will take in a `first_name`, `surname`, and `age`, and insert the student into the database.

Our SQL should look like this:

```sql
INSERT INTO students (first_name, surname, age) VALUES ("John", "McCollum", 38)
```

```python
def insert_student(first_name, surname, age):
    sql = f"""
        INSERT INTO students (first_name, surname, age)
        VALUES ("{first_name}", "{surname}", {age})
    """
    cursor.execute(sql)
    connection.commit()

```

Here, we're using string formatting to replace each `{}` in the string, in order. We could use string concatenation to do this, but this is much easier to read. With concatenation, it would be really easy to get our single quotes and double quotes mixed up.

Note that we don't need to use _any_ quotes at all for the student's age - this is because it's an integer. We use quotes for `TEXT` fields, otherwise, we don't need quotes at all.

Then, we execute our statement with `cursor.execute(sql)`, and `connection.commit()`.

We can similarly write functions to retrieve all students, or search for a student:

```python
def get_all_students():
    sql = "SELECT * FROM students"
    rows = cursor.execute(sql)
    return rows.fetchall()

def student_search(surname):
    sql = f"SELECT * FROM students WHERE surname='{surname}'"
    row = cursor.execute(sql)
    return row.fetchone()
```

In these cases, we're using the return value of `cursor.execute(sql)`. This lets us use the cursor's `fetchone()` or `fetchall()` methods. These will return a tuple of values, or a list of tuples respectively.

At this point, we should think through how we're going to use this data. The data format we get back isn't ideal; if we get back a tuple of values, we're going to have to access those values by index. For example:

```python
student = student_search("Bell")
id = student[0]
first_name = student[1]
```

We can do better than this.

Let's create a class for our Student.

```bash
touch student.py
```

```python
# student.py

class Student:
  def __init__(self, id, first_name, surname, age):
    self.id = id
    self.first_name = first_name
    self.surname = surname
    self.age = age
```

Near the top of our file, let's import student.

```python
import sqlite3
from student import * # ADDED
connection = sqlite3.connect("./students.db")
cursor = connection.cursor()

```

Now, let's update our methods that return students from the database:

```python
def get_all_students():
    sql = "SELECT * FROM students"
    rows = cursor.execute(sql)
    student_rows = rows.fetchall()
    return [Student(*student_row) for student_row in student_rows]

def student_search(surname):
    sql = f"SELECT * FROM students WHERE surname='{surname}'"
    row = cursor.execute(sql)
    student_row = row.fetchone()
    return Student(*student_row)
```

**Remember, doing `*student_row` is the same as doing `Student(student_row[0], student_row[1],student_row[2],student_row[3])`.** It expands a list / tuple into positional arguments.

Finally, for now, let's write a function to update a student's age. This will take in the ID of the student to update, and their new age.

```python
def update_student(id, new_age):
    sql = f"UPDATE students SET age={new_age} WHERE id={id}"
    cursor.execute(sql)
    connection.commit()
```

## Using our database

Now if we want to interact with our database, it's just a case of calling these functions!

```python
set_up_table()
insert_student("John", "McCollum", 38)
insert_student("Colin", "Bell", 35)
```

Now that this is done, we could present a series of options to the user:

```python
choice = ""
while choice.casefold() != "q":
    print("""
        Select an option:
        1. Display all Students
        2. Search for a student
        3. Update student's age
        """)

    choice = input()
```

Notice that we're setting up an infinite loop here - this means that after each option is selected, the program will keep running and we can see the results of our actions.

We can get the user's choice by calling the `input()` function.

Next, we can set up an `if` statement to check what the user entered, and respond accordingly.

```python
if choice == "1":
    all_students = get_all_students()
    for student in all_students:
        print(f"Student {student.id}: {student.first_name} {student.surname}, {student.age}")
elif choice == "2":
    pass
elif choice == "3":
    pass
```

A couple of things to note here. We're using `pass` as a placeholder, so that we can do something later.

Secondly, we're looping over the returned value from `get_all_students()`. This is possible because this function is returning a list of objects.

### Lab - 30 minutes

Use the functions we've written along with `input()` to complete the functionality for parts two and three, above.

Possible solution:

```python
if choice == "1":
    all_students = get_all_students()
    for student in all_students:
        print(f"Student {student.id}: {student.first_name} {student.surname}, {student.age}")

elif choice == "2":
    print("Enter Student Surname:")
    surname = input()
    student = student_search(surname)
    print(f"Student {student.id}: {student.first_name} {student.surname}, {student.age}")

elif choice == "3":
    print("Enter the student's surname:")
    surname = input()
    student = student_search(surname)

    if student is not None:
        print("Enter the student's new age:")
        age = input()

        update_student(student.id, age)
        print(f"{student.first_name} {student.surname} updated!")
    else:
        print("Student not found")
```
