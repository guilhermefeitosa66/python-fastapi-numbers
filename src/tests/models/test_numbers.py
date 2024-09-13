import pytest
from src.packages.numbers.models.numbers import Numbers


@pytest.fixture
def numbers_instance():
    return Numbers()


def test_sum_empty_list(numbers_instance):
    assert numbers_instance.sum([]) == 0


def test_sum_single_element(numbers_instance):
    assert numbers_instance.sum([5]) == 5


def test_sum_multiple_elements(numbers_instance):
    assert numbers_instance.sum([1, 2, 3, 4, 5]) == 15


def test_average_empty_list(numbers_instance):
    with pytest.raises(ZeroDivisionError):
        numbers_instance.average([])


def test_average_single_element(numbers_instance):
    assert numbers_instance.average([5]) == 5.0


def test_average_multiple_elements(numbers_instance):
    assert numbers_instance.average([1, 2, 3, 4, 5]) == 3.0
