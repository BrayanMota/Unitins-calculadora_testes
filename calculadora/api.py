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
    if numero2 == 0:
        return {"Resultado da Divisão": "Não é possível dividir por zero"}
    return {"Resultado da Divisão": f"{numero1 / numero2}"}


@calculadora.get("/raiz")
def raiz(numero1: int):
    if numero1 < 0:
        return {"Resultado da Raiz": "Não é possível calcular a raiz de número negativo"}
    return {"Resultado da Raiz": f"{numero1 ** (1/2)}"}


@calculadora.get("/potencia")
def potencia(numero1: int, numero2: int):
    return {"Resultado da Potência": f"{numero1 ** numero2}"}


@calculadora.get("/fatorial")
def fatorial(numero1: int):
    if numero1 < 0:
        return {"Resultado da Fatorial": "Não é possível calcular o fatorial de número negativo"}
    elif numero1 == 0:
        return {"Resultado da Fatorial": "O fatorial de 0 é 1"}
    else:
        resultado = 1
        for i in range(1, numero1 + 1):
            resultado *= i
        return {"Resultado da Fatorial": f"{resultado}"}
