# Lab

Take a look at the provided CSV file, employees.csv. It has a number of columns - `first_name`, `last_name`, `hourly_rate`, `hours_worked`, and `amount_due` ( which is currently zero.)

Perform the following tasks:

- Add a new employee to the file, with the following details:
	- first_name: Jenny
	- second_name: Jones
	- hourly_rate: 12.50
	- hours_worked: 40
- Loop through the employees, calculate the amount_due column (`hourly_rate * hours_worked`), and amend each row to add this data in the `amount_due` column.

_Handy Hint 1_: Think about the types of the data when you perform operations. You're always going to get a `String` back from a CSV file.

_Handy Hint 2_: Don't worry about formatting `amount_due` in a particular way.
