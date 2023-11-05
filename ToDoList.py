class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        print("\nTasks:")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. Description: {task.description}")
            print(f"   Due Date: {task.due_date}")
            print(f"   Priority: {task.priority}")
            print(f"   Status: {'Completed' if task.completed else 'Not Completed'}")
            print()

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.completed = True
            self.completed_tasks.append(task)
            self.tasks.pop(task_index)
            print("Task completed!")
        else:
            print("Invalid task index.")

    def update_task(self, task_index, new_description, new_due_date, new_priority):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.description = new_description
            task.due_date = new_due_date
            task.priority = new_priority
            print("Task updated!")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
            print("Task removed!")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Complete Task")
        print("4. Update Task")
        print("5. Remove Task")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            priority = input("Enter priority: ")
            task = Task(description, due_date, priority)
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.display_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as completed: ")) - 1
            todo_list.complete_task(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task index to update: ")) - 1
            new_description = input("Enter new description: ")
            new_due_date = input("Enter new due date: ")
            new_priority = input("Enter new priority: ")
            todo_list.update_task(task_index, new_description, new_due_date, new_priority)
        elif choice == "5":
            task_index = int(input("Enter the task index to remove: ")) - 1
            todo_list.remove_task(task_index)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
