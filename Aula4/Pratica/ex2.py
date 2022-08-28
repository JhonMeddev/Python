"""
- Escreva um algoritmo que leia dois valores numéricos e
que pergunte ao usuário qual operação ele deseja realizar:
adição(+), subtração(-), multiplicação(*), ou divisão(/).
Exiba na tela o resultado da operação desejada
-Repita até que a opção saída seja escolhida
(exercício da apostila - aula 3)
"""

print("CALCULADOR")
print("+ Adição")
print("- Subtração")
print("* Multiplicação")
print("/ Divisão")
print("Digite s para sair")

op = input("Qual operação deseja fazer ? : ")
if op == "+" or op == "-" or op == "*" or op == "/":
    x = int(input("Digite o primeiro valor: "))
    y = int(input("Digite o segundo valor: "))

while ( op != "s"):
    if (op == "+"):
        res = x + y
        print("Resultado: {} + {} = {}".format(x, y, res))
    elif (op == "-"):
        res = x - y
        print("Resultado: {} + {} = {}".format(x, y, res))
    elif (op == "*"):
        res = x * y
        print("Resultado: {} + {} = {}".format(x, y, res))
    elif (op == "/"):
        res = x / y
        print("Resultado: {} + {} = {}".format(x, y, res))
    else:
        print("Operação inválida!")

    op = input("Qual operação deseja fazer ? : ")
    if op == "+" or op == "-" or op == "*" or op == "/":
        x = int(input("Digite o primeiro valor: "))
        y = int(input("Digite o segundo valor: "))

print("Encerrando programa ....")