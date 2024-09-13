from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from src.packages.numbers.controllers.numbers_controller import NumbersController


app = FastAPI()

@app.get("/")
def health_check():
    return JSONResponse({"message": "OK"}, status_code=status.HTTP_200_OK)

app.include_router(
    router=NumbersController().router,
    tags=["numbers"],
    prefix="/api/v1/numbers"
)

@app.exception_handler(Exception)
def default_exception_handler(_: Request, exc: Exception):
    return JSONResponse(status_code=422, content={"message": "Seu pedido não pode ser processado", "error": str(exc)})
