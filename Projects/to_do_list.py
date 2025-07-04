import random

tasks = []

def add_task():
    task = {"ID": None, "name": "", "desc": "", "status": "", "tag": ""}
    task["ID"] = random.randint(1, 10000)
    task["name"] = input("Enter the name of your task: ").lower().strip()
    task["desc"] = input("Enter the description of your task: ").lower().strip()

    while True:
        task["status"] = input("Is your task 'new' or 'completed'? ").lower().strip()
        if task["status"] in ["new", "completed"]:
            break
        print("Invalid value. Please enter 'new' or 'completed'.")

    while True:
        task["tag"] = input("Enter the tag of your task (high or low): ").lower().strip()
        if task["tag"] in ["high", "low"]:
            break
        print("Invalid value. Please enter 'high' or 'low'.")

    tasks.append(task)
    print(f"\nTask successfully added:")
    print(f"ID: {task['ID']}\nName: {task['name']}\nDescription: {task['desc']}\nStatus: {task['status']}\nTag: {task['tag']}\n")


def search_task():
    search = input("Search your task by name or ID: ").lower().strip()
    for task in tasks:
        if str(task["ID"]) == search or task["name"] == search:
            print(f"\nTask found:")
            print(f"ID: {task['ID']}\nName: {task['name']}\nDescription: {task['desc']}\nStatus: {task['status']}\nTag: {task['tag']}\n")
            return
    print("Task not found.\n")


def delete_task():
    delete = input("Enter task name or ID to delete: ").lower().strip()
    for i, task in enumerate(tasks):
        if str(task["ID"]) == delete or task["name"] == delete:
            print(f"\nDeleting task:")
            print(f"ID: {task['ID']}\nName: {task['name']}\nDescription: {task['desc']}\nStatus: {task['status']}\nTag: {task['tag']}")
            tasks.pop(i)
            print("Task deleted.\n")
            return
    print("Task not found.\n")


def update_status():
    update = input("Enter task ID or name to update: ").lower().strip()
    for task in tasks:
        if str(task["ID"]) == update or task["name"] == update:
            print(f"Current status: {task['status']}")
            while True:
                new_status = input("Enter new status (new/completed): ").lower().strip()
                if new_status in ["new", "completed"]:
                    task["status"] = new_status
                    print("Status updated.\n")
                    return
                print("Invalid input. Please enter 'new' or 'completed'.")
    print("Task not found.\n")


def display_tasks():
    if not tasks:
        print("No tasks to display.\n")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"Task {i}:")
        print(f"ID: {task['ID']}\nName: {task['name']}\nDescription: {task['desc']}\nStatus: {task['status']}\nTag: {task['tag']}\n")


def filter_tag_status():
    filter_status = input("Filter by status (new/completed) or press Enter to skip: ").lower().strip()
    filter_tag = input("Filter by tag (high/low) or press Enter to skip: ").lower().strip()

    if filter_status not in ["new", "completed", ""]:
        print("Invalid status. Please enter 'new', 'completed', or leave blank.\n")
        return

    if filter_tag not in ["high", "low", ""]:
        print("Invalid tag. Please enter 'high', 'low', or leave blank.\n")
        return

    found = False
    for i, task in enumerate(tasks, start=1):
        status_match = (filter_status == "" or task["status"] == filter_status)
        tag_match = (filter_tag == "" or task["tag"] == filter_tag)

        if status_match and tag_match:
            print(f"Task {i}:")
            print(f"ID: {task['ID']}\nName: {task['name']}\nDescription: {task['desc']}\nStatus: {task['status']}\nTag: {task['tag']}\n")
            found = True

    if not found:
        print("No tasks match the selected filter.\n")


def show_stats():
    total = len(tasks)
    new_tasks = 0
    completed_tasks = 0
    high_tag = 0
    low_tag = 0

    for task in tasks:
        if task["status"] == "new":
            new_tasks += 1
        elif task["status"] == "completed":
            completed_tasks += 1

        if task["tag"] == "high":
            high_tag += 1
        elif task["tag"] == "low":
            low_tag += 1

    print("\n📊 Task Stats:")
    print(f"Total tasks: {total}")
    print(f"New tasks: {new_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"High-priority tasks: {high_tag}")
    print(f"Low-priority tasks: {low_tag}")


def show_menu():
    print("To-Do List Manager - Menu")
    print("1. Add a task")
    print("2. Search for a task")
    print("3. Delete a task")
    print("4. Update task status")
    print("5. Show all tasks")
    print("6. Filter tasks by tag/status")
    print("7. Show task stats")
    print("q. Quit")


while True:
    show_menu()
    choice = input("Choose an option: ").lower().strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        search_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        update_status()
    elif choice == "5":
        display_tasks()
    elif choice == "6":
        filter_tag_status()
    elif choice == "7":
        show_stats()
    elif choice == "q":
        print("Goodbye. See you next time.")
        break
    else:
        print("Invalid choice. Please try again.\n")
