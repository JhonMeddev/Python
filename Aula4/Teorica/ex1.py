"""
-Escreva um algoritmo que imprima na tela somente valores dentro de
um intevalo especificado pelo usuário e que sejam números pares
"""

inicial = int(input('Qual valor deseja iniciar a contagem ?'))
final = int(input('Qual valor deseja finalizar a contagem ?'))
x = inicial
while x <= final:
    if x % 2 == 0:
        print(x)
    x = x + 1
