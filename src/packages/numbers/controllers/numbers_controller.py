from fastapi import APIRouter

from src.packages.numbers.schemas.numbers_schemas import RequestAverageSchema, RequestSumSchema, ResponseAverageSchema, ResponseSumSchema
from src.packages.numbers.services.numbers_service import NumbersService


class NumbersController:
    def __init__(self):
        self.service = NumbersService()
        self.router = APIRouter()

        self.router.add_api_route(
            "/sum",
            self.sum,
            methods=["POST"],
            response_model=ResponseSumSchema,
        )

        self.router.add_api_route(
            "/average",
            self.average,
            methods=["POST"],
            response_model=ResponseAverageSchema,
        )

    def sum(self, params: RequestSumSchema):
        return self.service.sum(params.numbers)

    def average(self, params: RequestAverageSchema):
        return self.service.average(params.numbers)
