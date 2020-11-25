# Lab - Modules and Packages

## Learning Objectives
- practice breaking down code into modules and packages
- refactoring code to use functions

Using the start code provided, your task is to take the code in the file and break it down into modules and packages. The start code is for a task list. It has several functions for maintaining and displaying the list, and a main loop for running the actual program.

## Modules

1. Create a file `app.py` and move the main function loop into this file.

2. Create another file, called `output.py`. Move all the functions from `task_list.py` which perform no logic, but purely display information to the terminal (e.g. `print_task_descriptions()`) into `output.py`

3. Add `import` statements to `app.py` to import the code from `task_list.py` and `output.py`. Test your code works by running `app.py`

## Packages

1. Create a package called `modules` and move `task_list.py` and `output.py` into this package. Modify the `import` statements in `app.py` so that they import the modules from this package.

2. Create an empty file called `__init__.py` in your package.

## Extensions

1. Create a package called `data`. Inside this package create a file called `task_list.py`. Move the following code from the original `task_list.py` file into this file:

	```python
	tasks = [
    	{ "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    	{ "description": "Clean Windows", "completed": False, "time_taken": 15 },
    	{ "description": "Make Dinner", "completed": True, "time_taken": 30 },
    	{ "description": "Feed Cat", "completed": False, "time_taken": 5 },
    	{ "description": "Walk Dog", "completed": True, "time_taken": 60 },
	]
	```

2. Add another `import` statement to `app.py` to import the code from this module. (Remember to add your empty `__init__.py` file to your package).

3. In the main loop in `app.py` there is code which gets input from the user. Modify this code so that the `input` statements are replaced with calls to functions in a new module in the `modules` package called `modules` package called `input.py`. The code in `app.py` should now call these functions.

## Advanced Extension

Add code to `app.py` which asks the user if they want to load some tasks which have already been created. Make the `import` of the `tasks` from the module in the `data` package conditional so that it only imports the code if the user wants to. Otherwise the `tasks` list should start empty.

## Notes

Remember to `git commit` regularly. Before you do any commits you should create a `.gitignore` file which includes `__pycache__`


