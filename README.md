# Python CLI Calculator

## What Is This?

This is a command-line calculator built using Python. It can handle basic arithmetic operations, percentage calculations, and power values.

## Why I Built It

I built this project to practice Python basics like functions, user input, condition handling, and error handling. I also wanted to make a simple CLI project that I could improve step by step.

## Features

- addition
- subtraction
- multiplication
- division
- percentage calculation
- power calculation
- input validation
- division by zero handling
- invalid operation handling
- graceful exit on interrupted input
- clear screen option

## Project Structure

```text
python-calculator/
|-- main.py
|-- calculator.py
|-- README.md
`-- tests/
    `-- test_calculator.py
```

## How to Run

1. Open a terminal in the project folder.
2. Run:

```bash
python main.py
```

## How to Use

1. Enter the first number.
2. Choose an operation from the list.
3. Enter the second number.
4. View the result.
5. Choose whether to continue, clear the screen, or exit.

## Example

```text
Python Calculator
--------------------
Enter the first number: 25

Available operations:
  +   addition
  -   subtraction
  *   multiplication
  /   division
  %   percentage
  **  power
Choose an operation: %
Enter the percentage value: 40
Result: 10
```

## Tests

```bash
python -m unittest discover -s tests
```

## Future Improvements

- Add a GUI version
- Store data in a file or database
