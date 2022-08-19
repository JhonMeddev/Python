"""
- Escreva um algoritmo que leia dois valores numéricos e
que pergunte ao usuário qual operação ele deseja realizar:
adição(+), subtração(-), multiplicação(*), ou divisão(/).
Exiba na tela o resultado da operação desejada(exercício da apostila - aula 3)
"""

N1 = int(input("Digite o 1ª numero:"))
N2 = int(input("Digite o 2ª numero:"))
operacao = input("Digite o simbolo da operação que deseja: adição(+), subtração(-), multiplicação(*), ou divisão(/).")

if(operacao == "+"):
    res = N1 + N2
    print("O resultado é : {}".format(res))
elif(operacao == "-"):
    res = N1 - N2
    print("O resultado é : {}".format(res))
elif(operacao == "*"):
    res = N1 * N2
    print("O resultado é : {}".format(res))
elif(operacao == "/"):
    res = N1 / N2
    print("O resultado é : {}".format(res))
else:
    print("Esta operação não existe!")