from fastapi import FastAPI
from calculadora.api import calculadora

app = FastAPI()

app.include_router(calculadora, prefix="/api")

# sair = False
# lista = []

# print("Calculadora")

# def operadores():
#     print('------------------------------------------------------')
#     print('Operadores:')
#     print("1 - +")
#     print("2 - -")
#     print("3 - *")
#     print("4 - /")
#     print('5 - Resultado')
#     print("6 - Sair")
#     operador = input('Escolha um operador: ')
#     if operador == 1:
#         lista.append('+')
#     elif operador == 2:
#         lista.append('-')
#     elif operador == 3:
#         lista.append('*')
#     elif operador == 4:
#         lista.append('/')
#     elif operador == 5:
#         pass
#     elif operador == 6:
#         print("Saindo")
#         sair = True
#     else:
#         print("Opção inválida")
#     return

# while not sair:
#     print("1 - Inserir número")
#     print("2 - Listar números")
#     print("3 - Sair")
#     opcao = int(input("Digite uma opção: "))
#     if opcao == 1:
#         numero = int(input("Digite um número: "))
#         lista.append(str(numero))
#         print(numero)
#         operadores()
#     elif opcao == 2:
#         print(lista)
#     elif opcao == 3:
#         print("Saindo")
#         sair = True
#     else:
#         print("Opção inválida")

