import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_multiply_positive(self):
        assert self.calc.multiply(2, 3) == 6

    def test_division_positive(self):
        assert self.calc.division(10, 5) == 2

    def test_subtraction_positive(self):
        assert self.calc.subtraction(8, 3) == 5

    def test_adding_positive(self):
        assert self.calc.adding(4, 5) == 9