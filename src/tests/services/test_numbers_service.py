import pytest
from src.packages.numbers.services.numbers_service import NumbersService
from src.packages.numbers.schemas.numbers_schemas import ResponseSumSchema, ResponseAverageSchema


@pytest.fixture
def numbers_service():
    return NumbersService()


def test_sum(numbers_service):
    numbers = [1, 2, 3, 4, 5]
    response = numbers_service.sum(numbers)
    assert isinstance(response, ResponseSumSchema)
    assert response.result == 15


def test_sum_empty_list(numbers_service):
    numbers = []
    response = numbers_service.sum(numbers)
    assert isinstance(response, ResponseSumSchema)
    assert response.result == 0


def test_average(numbers_service):
    numbers = [1, 2, 3, 4, 5]
    response = numbers_service.average(numbers)
    assert isinstance(response, ResponseAverageSchema)
    assert response.result == 3.0


def test_average_empty_list(numbers_service):
    numbers = []
    with pytest.raises(ZeroDivisionError):
        numbers_service.average(numbers)
