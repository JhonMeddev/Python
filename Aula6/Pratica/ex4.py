"""
-Crie um jogo de pedra, papel ou tesoura(Jokenpô).
Você deverá jogar contra o computador. Você irá sempre escolher uma
das opções: 1-pedra, 2-papel, 3-tesoura.
-O computador irá sempre sortear um número de 1 até 3 para jogar
-Armazene todos os resultados em uma lista e no final apresente o vencedor
-Encerre o programa ao digitar zero
"""
#Biblioteca para gerar numeros aleatorio
import random

#FUNÇÕES

#Valida inteiro
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

#Verificar vencedor
def vencedor(jogador1, jogador2):
    #Trazendo variaveis global
    global empate, v1, v2
    if jogador1 == 1 : #Pedra
        if jogador2 == 1: #Pedra
            empate += 1
        elif jogador2 == 2: #Papel
            v2 += 1
        elif jogador2 == 3: #Tesoura
            v1 += 1
    elif jogador1 == 2: #Papel
        if jogador2 == 1: #Pedra
            v1 += 1
        elif jogador2 == 2: #Papel
            empate += 1
        elif jogador2 == 3: #Tesoura
            v2 += 1
    elif jogador1 == 3: #Tesoura
        if jogador2 == 1: #Pedra
            v2 += 1
        elif jogador2 == 2: #Papel
            v1 += 1
        elif jogador2 == 3: #Tesoura
            empate += 1
    resultados = [v1, v2, empate]
    return resultados

#Programa principal
print("=========JOKENPÔ=========")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")
print("0 - SAIR")

resultados = []
jogadas = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = valida_int('Escola sua jogada: ', 0, 3)
    if j1 == 0:
        break
    j2 = random.randint(1,3)
    # append(item) - adiciona um item ao final da lista
    jogadas.append([j1, j2])
    resultados = vencedor(j1, j2)

    for jogada in jogadas:
        for dado in jogada:
            print(dado, end=' ')
        print()
print('Numero de vitorias: {} \nNumero de percas: {} \nNumero de empates: {} '.format(v1, v2, empate))




