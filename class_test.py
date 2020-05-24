# class_test.py

import pytest


def sum(num1, num2):
    return num1 + num2


def divide(num1, num2):
    return num1 / num2


class TestDemo():
    def test_sum(self):
        assert sum(40, 2) == 42

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)
