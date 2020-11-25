from collections import namedtuple
import csv

Employee = namedtuple("Employee", "first_name last_name hourly_rate hours_worked amount_due")

# Append a new row
with open("employees.csv", "a") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    details = ["Jenny", "Jones", "12.50", "40", "0"]
    new_employee = Employee(*details)
    writer.writerow(new_employee)

# read all employee data in preparation for changing column
with open("employees.csv") as csvfile:
    reader = csv.reader(csvfile)
    all_employees = []
    
    next(reader)
    for row in reader:
        row = [column.strip().replace('"', '') for column in row]
        employee = Employee(*row)
        all_employees.append(employee)

# Calculate amount_due
with open("employees.csv", "w") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

    writer.writerow(["first_name", "last_name", "hourly_rate", "hours_worked", "amount_due"])
    for employee in all_employees:
        amount_due = float(employee.hourly_rate) * int(employee.hours_worked)
        modified_employee = Employee(employee.first_name, employee.last_name, employee.hourly_rate, employee.hours_worked, amount_due)
        writer.writerow(modified_employee)
