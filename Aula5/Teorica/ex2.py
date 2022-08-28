"""
-Escreva uma função para validar uma string.
Essa função recebe como parâmetro a string, o número mínimo
e máximo de caracteres.
Retorne verdadeiro se o tamanho da string estiver entre valores de
mínimo e máximo, e falso, caso contrário(elaborado com base
em Menezes, s. d.)
"""

#Função:
def validaString(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while ((tam < min) or (tam > max)):
        s1 = input(pergunta)
        tam = len(s1)
    return s1

#Programa Principal:
x = validaString('Digite uma string: ', 10, 30)
print("Vocês digitou a string: {}. \n Dado válido. Encerrando o programa...".format(x))
