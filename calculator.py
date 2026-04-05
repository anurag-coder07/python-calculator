"""Simple command-line calculator built with Python."""

from os import name, system


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


def percentage(first_number: float, second_number: float) -> float:
    return (first_number * second_number) / 100


def power(first_number: float, second_number: float) -> float:
    return first_number ** second_number


OPERATIONS = {
    "+": ("Addition", add),
    "-": ("Subtraction", subtract),
    "*": ("Multiplication", multiply),
    "/": ("Division", divide),
    "%": ("Percentage", percentage),
    "**": ("Power", power),
}


def clear_screen() -> None:
    system("cls" if name == "nt" else "clear")


def print_header() -> None:
    print("Python Calculator")
    print("-" * 20)


def format_result(result: float | int) -> str:
    numeric_result = float(result)
    if numeric_result.is_integer():
        return str(int(numeric_result))

    formatted_result = f"{numeric_result:.10f}".rstrip("0").rstrip(".")
    return "0" if formatted_result == "-0" else formatted_result


def get_number(prompt: str) -> float:
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def display_operations() -> None:
    print("\nAvailable operations:")
    print("  +   addition")
    print("  -   subtraction")
    print("  *   multiplication")
    print("  /   division")
    print("  %   percentage")
    print("  **  power")


def get_operation() -> str:
    display_operations()

    while True:
        operation = input("Choose an operation: ").strip()
        if operation in OPERATIONS:
            return operation
        print("Invalid operation. Please choose one from the list.")


def get_second_prompt(operation: str) -> str:
    if operation == "%":
        return "Enter the percentage value: "
    if operation == "**":
        return "Enter the power value: "
    return "Enter the second number: "


def calculate(first_number: float, second_number: float, operation: str) -> float:
    return OPERATIONS[operation][1](first_number, second_number)


def get_next_action() -> str:
    while True:
        action = input(
            "\nChoose an option: [y] another calculation, [c] clear screen, [n] exit: "
        ).strip().lower()

        if action in {"y", "c", "n"}:
            return action

        print("Please type y, c, or n.")


def main() -> None:
    print_header()

    while True:
        first_number = get_number("Enter the first number: ")
        operation = get_operation()
        second_number = get_number(get_second_prompt(operation))

        try:
            result = calculate(first_number, second_number, operation)
            print(f"Result: {format_result(result)}")
        except ZeroDivisionError as error:
            print(error)

        next_action = get_next_action()
        if next_action == "c":
            clear_screen()
            print_header()
            continue
        if next_action == "n":
            print("Thank you for using the calculator.")
            break


if __name__ == "__main__":
    main()
