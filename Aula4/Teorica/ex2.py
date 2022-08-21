"""
-Escreva um algoritmo que calcule a sua média de notas
em determinada disciplina

-Vamos assumir que é a média final é dada pela média
aritmética de cinco notas digitadas
"""
soma = 0
cont = 1
while cont <= 5:
    nota = float(input('Qual foi a sua nota {} ?'.format(cont)))
    soma = soma + nota
    cont = cont + 1
media = soma / 5
print('Sua nota final é : {}'.format(media))
