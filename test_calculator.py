import pytest
from calculator import Calculator

class TestCalculator:

    def test_sum(self):
        calculator = Calculator()
        assert calculator.sum() == 0
        calculator.op1 = 1
        assert calculator.sum() == 1
        calculator.op2 = 2
        assert calculator.sum() == 3
        calculator.op2 = 2.14
        assert calculator.sum() == 3.14

    def test_subtract(self):
        calculator = Calculator()
        assert calculator.subtract() == 0
        calculator.op1 = 1
        assert calculator.subtract() == 1
        calculator.op2 = 1
        assert calculator.subtract() == 0
        calculator.op2 = 2
        assert calculator.subtract() == -1
        calculator.op1 = 0.3
        calculator.op2 = 0.2
        assert round(calculator.subtract(),1) == 0.1

    def test_multiply(self):
        calculator = Calculator()
        assert calculator.multiply() == 0
        calculator.op1 = 1
        assert calculator.multiply() == 0
        calculator.op2 = 2
        assert calculator.multiply() == 2
        calculator.op1 = 0.1
        calculator.op2 = 0.2
        assert round(calculator.multiply(),2) == 0.02

    def test_divide_zero_div(self):
        with pytest.raises(ZeroDivisionError):
            calculator = Calculator()
            calculator.divide()

    def test_divide(self):
        calculator = Calculator(1, 1)
        assert calculator.divide() == 1
        calculator.op2 = 2
        assert calculator.divide() == 0.5
