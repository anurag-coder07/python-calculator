"""Professional command-line calculator built with Python."""


def add(first_number: float, second_number: float) -> float:
    return first_number + second_number


def subtract(first_number: float, second_number: float) -> float:
    return first_number - second_number


def multiply(first_number: float, second_number: float) -> float:
    return first_number * second_number


def divide(first_number: float, second_number: float) -> float:
    if second_number == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return first_number / second_number


def get_number(prompt: str) -> float:
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_operation() -> str:
    operations = {"+", "-", "*", "/"}
    while True:
        operation = input("Choose an operation (+, -, *, /): ").strip()
        if operation in operations:
            return operation
        print("Invalid operation. Please choose one of +, -, *, /.")


def calculate(first_number: float, second_number: float, operation: str) -> float:
    if operation == "+":
        return add(first_number, second_number)
    if operation == "-":
        return subtract(first_number, second_number)
    if operation == "*":
        return multiply(first_number, second_number)
    return divide(first_number, second_number)


def main() -> None:
    print("Python Calculator")
    print("-" * 20)

    while True:
        first_number = get_number("Enter the first number: ")
        operation = get_operation()
        second_number = get_number("Enter the second number: ")

        try:
            result = calculate(first_number, second_number, operation)
            print(f"Result: {result}")
        except ZeroDivisionError as error:
            print(error)

        continue_choice = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if continue_choice != "y":
            print("Thank you for using the calculator.")
            break


if __name__ == "__main__":
    main()
