# To-Do List Application

# Function to display the current to-do list
def display_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Function to add a new task to the to-do list
def add_task(tasks, new_task):
    tasks.append(new_task)
    print(f"Added: {new_task}")

# Function to update an existing task
def update_task(tasks, task_index, updated_task):
    if task_index >= 1 and task_index <= len(tasks):
        tasks[task_index - 1] = updated_task
        print(f"Task {task_index} updated.")
    else:
        print("Invalid task index.")

# Function to remove a task from the to-do list
def remove_task(tasks, task_index):
    if task_index >= 1 and task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Removed: {removed_task}")
    else:
        print("Invalid task index.")

# Main function
def main():
    tasks = []
    print("Welcome to the To-Do List application!")

    while True:
        print("\nOptions:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Remove task")
        print("5. Quit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
        elif choice == '3':
            task_index = int(input("Enter the task number to update: "))
            updated_task = input("Enter the updated task: ")
            update_task(tasks, task_index, updated_task)
        elif choice == '4':
            task_index = int(input("Enter the task number to remove: "))
            remove_task(tasks, task_index)
        elif choice == '5':
            print("Thank you for using the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
