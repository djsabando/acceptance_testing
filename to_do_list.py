

class Task:
    def __init__(self, name, status="Pending", description=""):
        self.name = name
        self.status = status
        self.description = description

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for task in self.tasks:
            print(f"- {task.name} [{task.status}] - {task.description}")

    def mark_task_complete(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.status = "Done"
                print(f"Task '{task_name}' marked as completed.")
                return
        print(f"Task '{task_name}' not found.")

    def clear_tasks(self):
        self.tasks = []
        print("All tasks cleared.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n===== To-Do List Manager =====")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Clear the entire to-do list")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            task = Task(name, description=description)
            todo_list.add_task(task)
            print("Task added successfully.")

        elif choice == "2":
            if todo_list.tasks:
                print("Tasks:")
                todo_list.list_tasks()
            else:
                print("No tasks in the list.")

        elif choice == "3":
            task_name = input("Enter the name of the task to mark as completed: ")
            todo_list.mark_task_complete(task_name)

        elif choice == "4":
            confirmation = input("Are you sure you want to clear all tasks? (yes/no): ")
            if confirmation.lower() == "yes":
                todo_list.clear_tasks()

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
