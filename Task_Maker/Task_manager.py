class Task:
    def __init__(self, name, description, due_date, priority):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"Due Date: {self.due_date}\n"
            f"Priority: {self.priority}"
        )

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        print("\n--- Add New Task ---")
        name = input("Task Name: ")
        description = input("Description: ")
        due_date = input("Due Date (YYYY-MM-DD): ")
        priority = input("Priority (High/Medium/Low): ")

        new_task = Task(name, description, due_date, priority)
        self.tasks.append(new_task)
        print("Task added successfully!\n")

    def view_all_tasks(self):
        print("\n--- List of Tasks ---")
        if not self.tasks:
            print("No tasks available.\n")
        else:
            for task in self.tasks:
                print(task)
                print("-" * 30)

    def remove_task(self):
        task_name = input("\nEnter task name to remove: ")
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                print(f"Task '{task_name}' removed successfully!\n")
                return
        print("Task not found.\n")

    def view_task(self):
        task_name = input("\nEnter task name to view: ")
        for task in self.tasks:
            if task.name == task_name:
                print("\n--- Task Details ---")
                print(task)
                print()
                return
        print("Task not found.\n")

    def update_task(self):
        task_name = input("\nEnter task name to update: ")

        for task in self.tasks:
            if task.name == task_name:
                print("\nWhat do you want to update?")
                print("1. Name")
                print("2. Description")
                print("3. Due Date")
                print("4. Priority")

                choice = input("Choose an option: ")

                if choice == "1":
                    task.name = input("New Name: ")
                elif choice == "2":
                    task.description = input("New Description: ")
                elif choice == "3":
                    task.due_date = input("New Due Date: ")
                elif choice == "4":
                    task.priority = input("New Priority: ")
                else:
                    print("Invalid choice.\n")
                    return

                print("Task updated successfully!\n")
                return

        print("Task not found.\n")


def main():
    manager = TaskManager()

    while True:
        print("===== TASK MANAGER MENU =====")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Single Task")
        print("4. Update Task")
        print("5. Remove Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_task()
        elif choice == "2":
            manager.view_all_tasks()
        elif choice == "3":
            manager.view_task()
        elif choice == "4":
            manager.update_task()
        elif choice == "5":
            manager.remove_task()
        elif choice == "6":
            print("Exiting Task Manager... Goodbye!")
            break
        else:
            print("Invalid option! Please try again.\n")


if __name__ == "__main__":
    main()
