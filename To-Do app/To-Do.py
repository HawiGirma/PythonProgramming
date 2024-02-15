#HAWI GIRMA MEGERSA ETS0644/15
#SKILL SPECTRUM
import addTask
import displayTask
import removeTasks
import sortTasks

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



def main():
    tasks = []
    completed_tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            task = input("Enter the task: ")
            addTask.add_task(task, tasks)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            removeTasks.remove_task(task, tasks)
        elif choice == '3':
            task = input("Enter the completed task: ")
            sortTasks.mark_completed(task, tasks, completed_tasks)
        elif choice == '4':
            displayTask.display_tasks(tasks, "Tasks")
        elif choice == '5':
            displayTask.display_tasks(completed_tasks, "Completed Tasks")
        elif choice == '6':
            removeTasks.remove_all_tasks(tasks)
        elif choice == '7':
            sortTasks.sort_tasks(tasks)
        elif choice == '8':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
