import pytest
from src.packages.numbers.models.number import Number


@pytest.fixture
def number():
    return Number()


def test_sum(number):
    assert number.sum(1, 2) == 3
    assert number.sum(-1, 1) == 0
    assert number.sum(-1, -1) == -2


def test_divide(number):
    assert number.divide(4, 2) == 2.0
    assert number.divide(9, 3) == 3.0
    assert number.divide(-6, 2) == -3.0


def test_divide_by_zero(number):
    with pytest.raises(ZeroDivisionError):
        number.divide(1, 0)
