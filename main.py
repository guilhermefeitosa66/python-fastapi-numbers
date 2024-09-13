from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


app = FastAPI()

@app.get("/")
def health_check():
    return JSONResponse({"message": "OK"}, status_code=status.HTTP_200_OK)

@app.exception_handler(Exception)
def default_exception_handler(_: Request, exc: Exception):
    return JSONResponse(status_code=422, content={"message": "Seu pedido não pode ser processado", "error": str(exc)})
