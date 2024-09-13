from pydantic import BaseModel


class RequestSumSchema(BaseModel):
    numbers: list[int]


class RequestAverageSchema(BaseModel):
    numbers: list[int]


class ResponseSumSchema(BaseModel):
    result: int


class ResponseAverageSchema(BaseModel):
    result: float
