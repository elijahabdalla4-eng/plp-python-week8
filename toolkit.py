
# My Python Toolkit
# This program provides three useful tools through a menu.

# Get a valid number from the user without crashing.
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")


# Tool 1: A simple calculator that performs basic arithmetic.
def calculator():
    print("\n--- Simple Calculator ---")
    first_number = get_number("Enter the first number: ")
    second_number = get_number("Enter the second number: ")

    print("Choose an operation: +, -, *, /")
    operation = input("Enter your operation: ").strip()

    if operation == "+":
        answer = first_number + second_number
    elif operation == "-":
        answer = first_number - second_number
    elif operation == "*":
        answer = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("Sorry, you cannot divide by zero.")
            return
        answer = first_number / second_number
    else:
        print("Invalid operation. Please choose +, -, *, or /.")
        return

    print(f"Your answer is: {answer}")


# Tool 2: A to-do list that lets users add, view, and remove tasks.
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to the main menu")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            task = input("Enter your task: ").strip()
            if task:
                tasks.append(task)
                print(f"Task added: {task}")
            else:
                print("Your task cannot be empty.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    number = int(input("Enter the task number to remove: "))
                    if 1 <= number <= len(tasks):
                        removed_task = tasks.pop(number - 1)
                        print(f"Removed task: {removed_task}")
                    else:
                        print("That task number does not exist.")
                except ValueError:
                    print("Please enter a valid whole number.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


# Tool 3: A number checker that identifies positive, negative, or zero.
def number_checker():
    print("\n--- Number Checker ---")
    number = get_number("Enter a number: ")

    if number > 0:
        print(f"{number} is a positive number.")
    elif number < 0:
        print(f"{number} is a negative number.")
    else:
        print("Your number is zero.")


# Main menu: Keep showing the tools until the user chooses Quit.
def main():
    print("Welcome to My Python Toolkit!")

    while True:
        print("\nPlease choose a tool:")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Checker")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            calculator()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            number_checker()
        elif choice == "4":
            print("Thank you for using My Python Toolkit. Goodbye!")
            break
        else:
            print(f"Sorry, '{choice}' is not a valid choice. Please enter 1, 2, 3, or 4.")


# Start the program.
if __name__ == "__main__":
    main()