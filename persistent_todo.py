import json
import os

FILE_NAME = "tasks_data.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

tasks = load_tasks()

while True:
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        if not tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
    elif choice == '2':
        task = input("Enter new task: ")
        if task.strip():
            tasks.append(task)
            save_tasks(tasks)
            print("Task added and saved successfully!")
        else:
            print("Task cannot be empty.")
    elif choice == '3':
        if not tasks:
            print("No tasks to delete.")
        else:
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
