tasks = []

while True:
    print("\n1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. View Tasks")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task Added Successfully")

    elif choice == 2:
        print(tasks)
        index = int(input("Enter task index: "))
        new_task = input("Enter updated task: ")
        tasks[index] = new_task
        print("Task Updated Successfully")

    elif choice == 3:
        task = input("Enter task to delete: ")
        tasks.remove(task)
        print("Task Deleted Successfully")

    elif choice == 4:
        print("Tasks:", tasks)

    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")