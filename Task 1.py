import os
import json
from datetime import datetime, timedelta

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
        return tasks
    else:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Task List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} - Priority: {task['priority']} - Due Date: {task['due_date']} - Completed: {task['completed']}")

def add_task(tasks, title, priority, due_date):
    task = {
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully.")

def remove_task(tasks, index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' removed successfully.")
    else:
        print("Invalid task index.")

def mark_completed(tasks, index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]['completed'] = True
        save_tasks(tasks)
        print(f"Task '{tasks[index - 1]['title']}' marked as completed.")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\n=== To-Do List ===")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            title = input("Enter task title: ")
            priority = input("Enter task priority (high/medium/low): ")
            due_date_str = input("Enter due date (YYYY-MM-DD) or leave blank: ")
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d') if due_date_str else None
            add_task(tasks, title, priority, due_date)
        elif choice == "3":
            display_tasks(tasks)
            index = int(input("Enter the index of the task to remove: "))
            remove_task(tasks, index)
        elif choice == "4":
            display_tasks(tasks)
            index = int(input("Enter the index of the task to mark as completed: "))
            mark_completed(tasks, index)
        elif choice == "5":
            save_tasks(tasks)
            print("Exiting. Your tasks are saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
