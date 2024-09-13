from src.packages.numbers.models.number import Number


class Numbers:
    def __init__(self):
        self.number = Number()

    def sum(self, numbers: list[int]) -> int:
        total = 0
        for n in numbers:
            total = self.number.sum(total, n)
        return total

    def average(self, numbers: list[int]) -> float:
        return self.number.divide(self.sum(numbers), len(numbers))
