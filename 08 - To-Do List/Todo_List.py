tasks = []


def show_tasks():

    if not tasks:
        print("\nNo tasks available.")
        return

    print("\nTO-DO LIST\n")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


while True:

    print("\n" + "=" * 40)
    print("         TO-DO LIST")
    print("=" * 40)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Clear All Tasks")
    print("0. Exit")

    try:

        choice = int(input("\nSelect Option: "))

        if choice == 1:

            task = input("Enter Task: ").strip()
   
            if task:
                tasks.append(task)
                print("✅ Task added successfully.")
            else:
                print("Task cannot be empty.")

        elif choice == 2:

            show_tasks()

        elif choice == 3:

            show_tasks()

            if tasks:
                task_no = int(input("\nEnter task number to remove: "))

                if 1 <= task_no <= len(tasks):
                    removed = tasks.pop(task_no - 1)
                    print(f"🗑️ '{removed}' removed.")
                else:
                    print("Invalid task number.")

        elif choice == 4:

            tasks.clear()
            print("✅ All tasks cleared.")

        elif choice == 0:

            print("\nGoodbye!")
            break

        else:
            print("Invalid option.")

    except ValueError:
        print("Please enter a valid number.")