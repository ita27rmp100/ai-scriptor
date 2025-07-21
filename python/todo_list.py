class Task:
    def __init__(self, title, description, done=False):
        self.title = title
        self.description = description
        self.done = done

    def mark_as_done(self):
        self.done = True

    def mark_as_undone(self):
        self.done = False


class ToDoList:
    def __init__(self):
        self.tasks = []

    def create_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Task '{title}' created.")

    def read_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Available tasks:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Done" if task.done else "Not done"
                print(f"{index}. {task.title} - {status}")

    def update_task(self, task_number, new_title=None, new_description=None):
        try:
            task = self.tasks[task_number - 1]
            if new_title:
                task.title = new_title
            if new_description:
                task.description = new_description
            print(f"Task {task_number} updated.")
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
            print(f"Task {task_number} deleted.")
        except IndexError:
            print("Invalid task number.")

    def mark_task_as_done(self, task_number):
        try:
            task = self.tasks[task_number - 1]
            task.mark_as_done()
            print(f"Task {task_number} marked as done.")
        except IndexError:
            print("Invalid task number.")

    def mark_task_as_undone(self, task_number):
        try:
            task = self.tasks[task_number - 1]
            task.mark_as_undone()
            print(f"Task {task_number} marked as not done.")
        except IndexError:
            print("Invalid task number.")


def main():
    todo = ToDoList()
    while True:
        print("\n1. Create task")
        print("2. Read tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Mark task as done")
        print("6. Mark task as not done")
        print("7. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo.create_task(title, description)
        elif choice == "2":
            todo.read_tasks()
        elif choice == "3":
            todo.read_tasks()
            task_number = int(input("Enter task number to update: "))
            new_title = input("Enter new task title (or press enter to skip): ")
            new_description = input("Enter new task description (or press enter to skip): ")
            todo.update_task(task_number, new_title or None, new_description or None)
        elif choice == "4":
            todo.read_tasks()
            task_number = int(input("Enter task number to delete: "))
            todo.delete_task(task_number)
        elif choice == "5":
            todo.read_tasks()
            task_number = int(input("Enter task number to mark as done: "))
            todo.mark_task_as_done(task_number)
        elif choice == "6":
            todo.read_tasks()
            task_number = int(input("Enter task number to mark as not done: "))
            todo.mark_task_as_undone(task_number)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
