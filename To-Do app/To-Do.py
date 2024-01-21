def display_menu():
    print("\n===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. Remove Specific Task")
    print("3. Mark Completed Task")
    print("4. Display Tasks")
    print("5. Display Completed Tasks")
    print("6. Remove All Tasks")
    print("7. Sort Tasks Alphabetically")
    print("8. Exit")

def add_task(task, task_list):
    task_list.append(task)
    print(f'Task "{task}" added successfully!')

def remove_task(task, task_list):
    if task in task_list:
        task_list.remove(task)
        print(f'Task "{task}" removed successfully!')
    else:
        print(f'Task "{task}" not found in the list.')

def mark_completed(task, task_list, completed_tasks):
    if task in task_list:
        task_list.remove(task)
        completed_tasks.append(task)
        print(f'Task "{task}" marked as completed!')
    else:
        print(f'Task "{task}" not found in the list.')

def display_tasks(task_list, header):
    if not task_list:
        print(f"{header} is empty.")
    else:
        print(f"{header}:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

def remove_all_tasks(task_list):
    task_list.clear()
    print("All tasks removed successfully!")

def sort_tasks(task_list):
    task_list.sort()
    print("Tasks sorted alphabetically!")

def main():
    tasks = []
    completed_tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task, tasks)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task, tasks)
        elif choice == '3':
            task = input("Enter the completed task: ")
            mark_completed(task, tasks, completed_tasks)
        elif choice == '4':
            display_tasks(tasks, "Tasks")
        elif choice == '5':
            display_tasks(completed_tasks, "Completed Tasks")
        elif choice == '6':
            remove_all_tasks(tasks)
        elif choice == '7':
            sort_tasks(tasks)
        elif choice == '8':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
