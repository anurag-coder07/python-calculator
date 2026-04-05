"""Tests for the calculator module."""

import unittest

from calculator import calculate, divide, format_result, percentage, power


class CalculatorTests(unittest.TestCase):
    def test_percentage_operation(self) -> None:
        self.assertEqual(percentage(250, 10), 25)

    def test_power_operation(self) -> None:
        self.assertEqual(power(3, 4), 81)

    def test_divide_by_zero_raises_error(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_calculate_uses_requested_operation(self) -> None:
        self.assertEqual(calculate(7, 8, "+"), 15)
        self.assertEqual(calculate(12, 25, "%"), 3)
        self.assertEqual(calculate(2, 5, "**"), 32)

    def test_format_result_removes_extra_zeroes(self) -> None:
        self.assertEqual(format_result(15.0), "15")
        self.assertEqual(format_result(3.5), "3.5")


if __name__ == "__main__":
    unittest.main()
