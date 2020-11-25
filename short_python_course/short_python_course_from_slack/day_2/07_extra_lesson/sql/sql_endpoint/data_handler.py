import sqlite3
from student import *

connection = sqlite3.connect("./students.db")
cursor = connection.cursor()


def set_up_table():
    cursor.execute("DROP TABLE IF EXISTS students")
    cursor.execute("""
        CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        surname TEXT,
        age INTEGER)
    """)
    connection.commit()

def insert_student(first_name, surname, age):
    sql = f"""
        INSERT INTO students (first_name, surname, age)
        VALUES ('{first_name}', '{surname}', {age})
    """
    cursor.execute(sql)
    connection.commit()

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

def update_student(id, new_age):
    sql = f"UPDATE students SET age={new_age} WHERE id={id}"
    cursor.execute(sql)
    connection.commit()

set_up_table()
insert_student("John", "McCollum", 38)
insert_student("Colin", "Bell", 35)

choice = ""
while choice.casefold() != "q":
    print("""
        Select an option:
        1. Display all Students
        2. Search for a student
        3. Update student's age

        Press `q` to quit
        """)
    choice = input()


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
