import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator

class TestCalculator(unittest.TestCase):

    def test_add_two_numbers(self):
        self.assertEqual(calculator.add_two_numbers(2, 3), 5)
        self.assertEqual(calculator.add_two_numbers(5, 0), 5)
        self.assertEqual(calculator.add_two_numbers(-1, 1), 0)
        self.assertEqual(calculator.add_two_numbers(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(2, 3), -1)
        self.assertEqual(calculator.subtract(5, 0), 5)
        self.assertEqual(calculator.subtract(-1, 1), -2)
        self.assertEqual(calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(5, 0), 0)
        self.assertEqual(calculator.multiply(-1, 1), -1)
        self.assertEqual(calculator.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 5), 2)
        self.assertEqual(calculator.divide(5, 2), 2.5)
        self.assertEqual(calculator.divide(-8, 2), -4)
        self.assertEqual(calculator.divide(-12, -4), 3)
        self.assertEqual(calculator.divide(3, 1), 3)

    def test_add_three_numbers(self):
        self.assertEqual(calculator.add_three_numbers(2, 3, 5), 10)
        self.assertEqual(calculator.add_three_numbers(5, 0, -1), 4)
        self.assertEqual(calculator.add_three_numbers(-1, -1, -1), -3)
        self.assertEqual(calculator.add_three_numbers(-1, -1, 100), 98)

    def test_power(self):
        self.assertEqual(calculator.power(4, 2), 16)
        self.assertEqual(calculator.power(3, 0), 1)
        self.assertEqual(calculator.power(0, 7), 0)
        self.assertEqual(calculator.power(-3, 3), -27)
        self.assertEqual(calculator.power(-2, 4), 16)
        self.assertEqual(calculator.power(5, -2), 0.04)
        self.assertEqual(calculator.power(5, 1), 5)

if __name__ == '__main__':
    unittest.main()