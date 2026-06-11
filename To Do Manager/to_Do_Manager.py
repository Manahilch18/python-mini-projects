tasks = []
try:
    with open("tasks.txt", "r") as file:
        for line in file:
            name, status, priority = line.strip().split("|")
            task = {
                "name": name,
                "status": status,
                "priority": priority
            }
            tasks.append(task)
except FileNotFoundError:
    pass
# Save Tasks
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(
                f"{task['name']}|{task['status']}|{task['priority']}\n"
            )
# Add Task
def add_task():
    name = input("Enter task name: ")
    priority = input(
        "Enter priority (High/Medium/Low): "
    ).capitalize()
    task = {
        "name": name,
        "status": "Pending",
        "priority": priority
    }
    tasks.append(task)
    save_tasks()
    print("Task added successfully!") 
# View Tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    print("\n===== TASK LIST =====")
    for index, task in enumerate(tasks, start=1):
        print(
            f"{index}. "
            f"{task['name']} | "
            f"Status: {task['status']} | "
            f"Priority: {task['priority']}"
        ) 
# Mark Task as Completed 
def mark_task_done():
    if not tasks:
        print(" No tasks available.")
        return
    view_tasks()
    try:
        task_number = int(
            input("\nEnter task number to complete: ")
        )
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["status"] = "Completed"
            save_tasks()
            print(" Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")
# Delete Task
def delete_task():
    if not tasks:
        print("No tasks available.")
        return
    view_tasks()
    try:
        task_number = int(
            input("\nEnter task number to delete: ")
        )
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            save_tasks()
            print(
                f" '{deleted_task['name']}' deleted successfully!"
            )
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")
# Search Task 
def search_task():
    keyword = input(
        "Enter keyword to search: "
    ).lower()
    found = False
    for index, task in enumerate(tasks, start=1):
        if keyword in task["name"].lower():
            print(
                f"{index}. "
                f"{task['name']} | "
                f"Status: {task['status']} | "
                f"Priority: {task['priority']}"
            )
            found = True
    if not found:
        print("No matching task found.") 
# Show Statistics
def show_statistics():
    total = len(tasks)
    completed = 0
    for task in tasks:
        if task["status"] == "Completed":
            completed += 1
    pending = total - completed
    print("\n===== TASK STATISTICS =====")
    print(f"Total Tasks     : {total}")
    print(f"Completed Tasks : {completed}")
    print(f"Pending Tasks   : {pending}") 
# MAIN MENU 
while True:
    print("\n=========================")
    print(" SMART TO-DO MANAGER ")
    print("=========================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Show Statistics")
    print("7. Exit")
    choice = input("\nEnter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        search_task()
    elif choice == "6":
        show_statistics()
    elif choice == "7":
        print(" Thanks for using Smart To-Do Manager!")
        break
    else:
        print("Invalid choice. Please try again.")