from modules.input import *
from modules.output import *
from modules.task_list import *

tasks = [
]

# EXTENSION
seed_data = input("Do you want to load some tasks (y/n)? ")
if seed_data.lower() == "y":
    from data.task_list import tasks

print_menu()
while (True):
    option = get_option_choice()
    if (option.lower() == 'q'):
        break
    elif (option.lower() == 'm'):
        print_menu()
    elif option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif option == '3':
        print_list(get_completed_tasks(tasks))
    elif option == '4':
        description = get_task_description()
        task = get_task_with_description(tasks, description)
        if task != "Task Not Found":
            mark_task_complete(task)
    elif option == '5':
        duration = get_duration()
        print_list(get_tasks_taking_longer_than(tasks, duration))
    elif option == '6':
        description = get_task_description()
        print(get_task_with_description(tasks, description))
    elif option == '7':
        description = input("Enter description: ")
        time_taken = int(input("Enter time taken: "))
        task = create_task(description, time_taken)
        add_to_list(tasks, task)
    else:
        print("Invalid Input - choose another option")
