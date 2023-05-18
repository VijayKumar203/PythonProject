def display_menu():
    """
    Displays the menu options for the to-do list.
    """
    print("List for the task to select")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Exit")

def view_todo_list(todo_list):
    """
    Displays the current to-do list.
    """
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("===== To-Do List =====")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task(todo_list):
    """
    Prompts the user to add a new task to the to-do list.
    """
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added successfully!")

def complete_task(todo_list):
    """
    Prompts the user to complete a task from the to-do list.
    """
    if not todo_list:
        print("Your to-do list is empty.")
        return

    view_todo_list(todo_list)
    task_number = int(input("Enter the number of the task to complete: ")) - 1

    if 0 <= task_number < len(todo_list):
        completed_task = todo_list.pop(task_number)
        print(f"Task '{completed_task}' completed!")
    else:
        print("Invalid task number.")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_todo_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            complete_task(todo_list)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

    
