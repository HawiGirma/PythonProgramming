
def remove_task(task, task_list):
    if task in task_list:
        task_list.remove(task)
        print(f'Task "{task}" removed successfully!')
    else:
        print(f'Task "{task}" not found in the list.')

def remove_all_tasks(task_list):
    task_list.clear()
    print("All tasks removed successfully!")