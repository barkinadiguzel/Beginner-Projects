tasks = []

def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View tasks")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"Task '{task}' added.")
    elif choice == "2":
        show_tasks()
        if tasks:
            idx = int(input("Enter task number to remove: "))
            if 1 <= idx <= len(tasks):
                removed = tasks.pop(idx-1)
                print(f"Task '{removed}' removed.")
            else:
                print("Invalid task number.")
    elif choice == "3":
        show_tasks()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
