def get_option_choice():
    print()
    option = input("Select an option 1, 2, 3, 4, 5 or (Q)uit: ")
    return option

def get_task_description():
    description = input("Enter task description to search for: ")
    return description

def get_duration():
    duration = input("Enter task duration: ")
    return int(duration)
