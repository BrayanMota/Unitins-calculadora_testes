from fastapi import APIRouter, HTTPException, status

calculadora = APIRouter(tags=["Calculadora"])


@calculadora.get("/adicao")
def somar(numero1: int, numero2: int):
    return numero1 + numero2


@calculadora.get("/subtracao")
def subtrair(numero1: int, numero2: int):
    return numero1 - numero2


@calculadora.get("/multiplicacao")
def multiplicar(numero1: int, numero2: int):
    return numero1 * numero2


@calculadora.get("/divisao")
def dividir(numero1: int, numero2: int):
    if numero2 == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Não é possível dividir por zero")
    return numero1 / numero2


@calculadora.get("/raiz")
def raiz(numero: int):
    if numero < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Não é possível calcular a raiz de número negativo")
    return numero ** (1/2)


@calculadora.get("/potencia")
def potencia(numero1: int, numero2: int):
    return numero1 ** numero2


@calculadora.get("/fatorial")
def fatorial(numero: int):
    if numero < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Não é possível calcular o fatorial de número negativo")
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado
