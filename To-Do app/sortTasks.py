def sort_tasks(task_list):
    task_list.sort()
    print("Tasks sorted alphabetically!")

def mark_completed(task, task_list, completed_tasks):
    if task in task_list:
        task_list.remove(task)
        completed_tasks.append(task)
        print(f'Task "{task}" marked as completed!')
    else:
        print(f'Task "{task}" not found in the list.')
