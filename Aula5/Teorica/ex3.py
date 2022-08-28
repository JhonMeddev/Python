"""
-Função como prâmetro de função
"""

#Funções:
def imprimeComCondicao(num, fcond):
    if fcond(num):
        print(num)

def par(x):
    return x % 2 == 0
def impar(x):
    return not par(x)

#Programa principal
imprimeComCondicao(5, impar)