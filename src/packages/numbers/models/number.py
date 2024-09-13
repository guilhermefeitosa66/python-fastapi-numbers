class Number:
    def sum(self, a: int, b: int) -> int:
        return a + b

    def divide(self, a: int, b: int) -> float:
        try:
            return a / b
        except Exception as exc:
            raise exc
