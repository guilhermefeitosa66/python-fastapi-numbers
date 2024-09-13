from src.packages.numbers.models.numbers import Numbers
from src.packages.numbers.schemas.numbers_schemas import ResponseAverageSchema, ResponseSumSchema


class NumbersService:
    def __init__(self):
        self.model = Numbers()

    def sum(self, numbers: list[int]) -> ResponseSumSchema:
        result = self.model.sum(numbers)
        return ResponseSumSchema(result=result)

    def average(self, numbers: list[int]) -> ResponseAverageSchema:
        result = self.model.average(numbers)
        return ResponseAverageSchema(result=result)
