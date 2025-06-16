from my_project.calculator import Calculator
import pytest

@pytest.fixture
def calculation():
    # creates  a fresh istance of Calculator before each test
    return Calculator(10,5)


# failed
def test_addition(calculation):
    assert calculation.addition() == 13, "The sum is wrong"

# passed
def test_subtraction(calculation):
    assert calculation.subtraction() == 5, "the subtraction is wrong"

# passed
def test_multiplication(calculation):
    assert calculation.multiplication() == 50, "The multiplication is wrong"

# passed
def test_division(calculation):
    assert calculation.division() == 2.00, "The quotient is wrong"