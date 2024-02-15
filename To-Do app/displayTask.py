def display_tasks(task_list, header):
    if not task_list:
        print(f"{header} is empty.")
    else:
        print(f"{header}:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")