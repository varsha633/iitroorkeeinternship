TASK_FILE = "tasks.txt"

def add_task(task):
    with open(TASK_FILE, "a") as file:
        file.write(task + "\n")

def view_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks found.")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No task file found.")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
        print("Task added successfully!")
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
