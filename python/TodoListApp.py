class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_name):
        self.tasks[task_name] = False
        print(f"Task '{task_name}' added successfully.")

    def remove_task(self, task_name):
        if task_name in self.tasks:
            del self.tasks[task_name]
            print(f"Task '{task_name}' removed successfully.")
        else:
            print(f"Task '{task_name}' not found.")

    def mark_as_completed(self, task_name):
        if task_name in self.tasks:
            self.tasks[task_name] = True
            print(f"Task '{task_name}' marked as completed.")
        else:
            print(f"Task '{task_name}' not found.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task, status in self.tasks.items():
                status = "Completed" if status else "Pending"
                print(f"Task: {task}, Status: {status}")


def main():
    todo = ToDoList()
    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Mark as Completed")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task_name = input("Enter task name: ")
            todo.add_task(task_name)
        elif choice == "2":
            task_name = input("Enter task name: ")
            todo.remove_task(task_name)
        elif choice == "3":
            task_name = input("Enter task name: ")
            todo.mark_as_completed(task_name)
        elif choice == "4":
            todo.view_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
