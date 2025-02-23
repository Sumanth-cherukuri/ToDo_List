# Simple To-Do List

tasks = []

while True:
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        if tasks:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("\nYour to-do list is empty.")

    elif choice == '2':
        task = input("\nEnter a new task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == '3':
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_number = int(input("\nEnter task number to remove: "))
                if 0 < task_number <= len(tasks):
                    tasks.pop(task_number - 1)
                    print("Task removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a number.")
        else:
            print("\nNo tasks to remove.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
