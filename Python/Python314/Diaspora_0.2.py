import os  # We'll use this for checking if the file exists

# AI Generated
# --- Global Variable for our To-Do List ---
# Each to-do item will be a dictionary with 'task' and 'completed' keys.
# 'task' will store the description (string).
# 'completed' will store a boolean (True/False) indicating if it's done.
todos = []
TODO_FILE = "todos.txt"  # Name of the file to save/load tasks

# --- Functions for our To-Do Application ---


def load_todos():
    """Loads tasks from the TODO_FILE into the 'todos' list."""
    if os.path.exists(TODO_FILE):  # Check if the file exists
        try:
            with open(TODO_FILE, "r") as file:
                for line in file:
                    parts = line.strip().split('|')
                    if len(parts) == 2:
                        task_desc = parts[0]
                        # Convert 'True'/'False' string to boolean
                        completed_status = (parts[1].lower() == 'true')
                        todos.append(
                            {"task": task_desc, "completed": completed_status})
            print(f"Loaded {len(todos)} tasks from {TODO_FILE}.")
        except Exception as e:
            print(f"Error loading tasks: {e}")
    else:
        print("No existing to-do list found. Starting with an empty list.")


def save_todos():
    """Saves the current 'todos' list to the TODO_FILE."""
    try:
        with open(TODO_FILE, "w") as file:
            for item in todos:
                # Format: "task_description|True/False"
                file.write(f"{item['task']}|{item['completed']}\n")
        print(f"Saved {len(todos)} tasks to {TODO_FILE}.")
    except Exception as e:
        print(f"Error saving tasks: {e}")


def add_task():
    """Prompts the user for a task description and adds it to the list."""
    task_description = input("Enter the task description: ").strip()
    if task_description:  # Ensure the task description is not empty
        todos.append({"task": task_description, "completed": False})
        print(f"Task '{task_description}' added.")
        save_todos()  # Save after adding
    else:
        print("Task description cannot be empty.")


def view_tasks():
    """Displays all tasks in the list with their status."""
    if not todos:  # Check if the list is empty
        print("Your to-do list is empty!")
        return

    print("\n--- Your To-Do List ---")
    for i, item in enumerate(todos):  # enumerate gives both index and item
        status = "[X]" if item["completed"] else "[ ]"
        print(f"{i + 1}. {status} {item['task']}")
    print("-----------------------\n")


def mark_task_complete():
    """Allows the user to mark a task as complete."""
    view_tasks()  # First, show the tasks so the user knows the numbers
    if not todos:
        return  # Exit if no tasks to mark

    try:
        task_number = int(
            input("Enter the number of the task to mark as complete: "))
        # Adjust for 0-based indexing
        task_index = task_number - 1

        if 0 <= task_index < len(todos):
            todos[task_index]["completed"] = True
            print(f"Task '{todos[task_index]['task']}' marked as complete.")
            save_todos()  # Save after marking complete
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_task():
    """Allows the user to delete a task."""
    view_tasks()  # First, show the tasks so the user knows the numbers
    if not todos:
        return  # Exit if no tasks to delete

    try:
        task_number = int(input("Enter the number of the task to delete: "))
        task_index = task_number - 1

        if 0 <= task_index < len(todos):
            removed_task = todos.pop(task_index)  # Remove and get the item
            print(f"Task '{removed_task['task']}' deleted.")
            save_todos()  # Save after deleting
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")


def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")
    print("-----------------------")

# --- Main Application Loop ---


def main():
    """The main function to run the To-Do List application."""
    load_todos()  # Load tasks when the application starts

    while True:  # Infinite loop until user chooses to exit
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break  # Exit the while loop
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# This ensures that main() is called only when the script is executed directly
if __name__ == "__main__":
    main()
