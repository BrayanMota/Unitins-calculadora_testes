from fastapi import APIRouter

calculadora = APIRouter(tags=["Calculadora"])

@calculadora.get("/adicao")
def somar(numero1: int, numero2: int):
    return {"Resultado da Soma": f"{numero1 + numero2}"}

@calculadora.get("/subtracao")
def subtrair(numero1: int, numero2: int):
    return {"Resultado da Subtração": f"{numero1 - numero2}"}

@calculadora.get("/multiplicacao")
def multiplicar(numero1: int, numero2: int):
    return {"Resultado da Multiplicação": f"{numero1 * numero2}"}

@calculadora.get("/divisao")
def dividir(numero1: int, numero2: int):
    return {"Resultado da Divisão": f"{numero1 / numero2}"}
