tasks = []

def add_task(task):
    tasks.append(task)

def view_tasks():
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks.")

def delete_task(index):
    try:
        del tasks[index]
    except IndexError:
        print("Task not found.")

def main():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
