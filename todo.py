#To-do list Project
tasks = []
next_id = 1

#Adding a new task
def add_task():
    global next_id

    title = input("Enter task title: ")

    if title.strip() == "":
        print("Task title cannot be empty!")
        return

    task = {
        "id": next_id,
        "title": title,
        "status": "Pending"
    }

    tasks.append(task)
    next_id += 1

    print("Task added successfully!")

#view all task
def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
        return

    print("\n" + "=" * 55)
    print("                    YOUR TASKS")
    print("=" * 55)

    print(f"{'ID':<5}{'Title':<35}{'Status'}")
    print("-" * 55)

    for task in tasks:
        print(f"{task['id']:<5}{task['title']:<35}{task['status']}")

    print("=" * 55)

#Complete a task
def complete_task():
    if len(tasks) == 0:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        task_id = int(input("\nEnter task ID to mark as completed: "))

        for task in tasks:
            if task["id"] == task_id:

                if task["status"] == "Completed":
                    print("Task is already completed!")
                else:
                    task["status"] = "Completed"
                    print("Task marked as completed!")

                return

        print("Task ID not found.")

    except ValueError:
        print("Please enter a valid number.")

#Edit a task
def edit_task():
    if len(tasks) == 0:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        task_id = int(input("\nEnter task ID to edit: "))

        for task in tasks:
            if task["id"] == task_id:

                new_title = input("Enter new task title: ")

                if new_title.strip() == "":
                    print("Task title cannot be empty!")
                    return

                task["title"] = new_title

                print("Task updated successfully!")
                return

        print("Task ID not found.")

    except ValueError:
        print("Please enter a valid number.")

#Delete a task
def delete_task():
    if len(tasks) == 0:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        task_id = int(input("\nEnter task ID to delete: "))

        for task in tasks:
            if task["id"] == task_id:

                tasks.remove(task)

                print("Task deleted successfully!")
                return

        print("Task ID not found.")

    except ValueError:
        print("Please enter a valid number.")

#main function of a program
while True:

    print("\n" + "=" * 40)
    print("             TO-DO LIST")
    print("=" * 40)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Edit Task")
    print("5. Delete Task")
    print("6. Exit")

    print("=" * 40)

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        edit_task()

    elif choice == "5":
        delete_task()

    elif choice == "6":
        print("\nThank you for using the To-Do List!")
        print("Goodbye!")
        break

    else:
        print("\nInvalid choice! Please enter a number from 1 to 6.")