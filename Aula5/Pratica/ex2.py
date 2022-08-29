"""
-Escreva uma função que calcule o fatorial de um número recebido como
parâmetro e retorne o seu resultado

- Faça uma validação dos dados por meio de umas outra função,
permitindo que somente valores positivos sejam aceitos

-Crie o help da sua função
"""

#Fatorial de 5 : 5x4; 20x3; 60x2; 120x1
#Fatorial de 0 é 1

def validacao(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def fatorial(num):
    """
    Calcular a fotorial
    :param num: parametro inteiro
    :return: retorna 1 para parametro 0 ou fatorial para parametro > 0
    """
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num+1, 1):
        fat = fat * i
    return fat



#Programa principal
x = validacao('Digite um valor POSITIVO para calcular o fatorial: ', 0, 99999)
print('Fatorial de {} é = {}'.format(x, fatorial(x)))
help(fatorial)