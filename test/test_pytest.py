import pytest
from src import calculator

def test_add_two_numbers():
    assert calculator.add_two_numbers(2, 3) == 5
    assert calculator.add_two_numbers(5,0) == 5
    assert calculator.add_two_numbers (-1, 1) == 0
    assert calculator.add_two_numbers (-1, -1) == -2

def test_subtract():
    assert calculator.subtract(2, 3) == -1
    assert calculator.subtract(5,0) == 5
    assert calculator.subtract (-1, 1) == -2
    assert calculator.subtract (-1, -1) == 0

def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(5,0) == 0
    assert calculator.multiply (-1, 1) == -1
    assert calculator.multiply (-1, -1) == 1

def test_divide():
    assert calculator.divide(10, 5) == 2
    assert calculator.divide(5, 2) == 2.5
    assert calculator.divide(-8, 2) == -4
    assert calculator.divide(-12, -4) == 3
    assert calculator.divide(3, 1) == 3

def test_add_three_numbers():
    assert calculator.add_three_numbers(2, 3, 5) == 10
    assert calculator.add_three_numbers(5,0, -1) == 4
    assert calculator.add_three_numbers (-1, -1, -1) == -3
    assert calculator.add_three_numbers (-1, -1, 100) == 98