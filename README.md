# Python CLI Calculator

A simple command-line calculator built using Python.

## Features

- addition
- subtraction
- multiplication
- division
- percentage calculation
- power calculation
- input validation
- division by zero handling
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
