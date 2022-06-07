from fastapi import FastAPI
from calculadora.api import calculadora

app = FastAPI()

app.include_router(calculadora, prefix="/api")
