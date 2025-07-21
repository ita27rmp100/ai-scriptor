class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self):
        task_name = input("Enter task name: ")
        self.tasks[task_name] = False
        print(f"Task '{task_name}' added.")

    def remove_task(self):
        task_name = input("Enter task name: ")
        if task_name in self.tasks:
            del self.tasks[task_name]
            print(f"Task '{task_name}' removed.")
        else:
            print(f"Task '{task_name}' not found.")

    def mark_task(self):
        task_name = input("Enter task name: ")
        if task_name in self.tasks:
            self.tasks[task_name] = True
            print(f"Task '{task_name}' marked as completed.")
        else:
            print(f"Task '{task_name}' not found.")

    def view_tasks(self):
        print("\nTo-Do List:")
        for task, status in self.tasks.items():
            status = "Completed" if status else "Not Completed"
            print(f"{task}: {status}")


def main():
    todo = ToDoList()
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Mark task as completed")
        print("4. View tasks")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            todo.add_task()
        elif choice == "2":
            todo.remove_task()
        elif choice == "3":
            todo.mark_task()
        elif choice == "4":
            todo.view_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
