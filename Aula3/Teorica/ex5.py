"""
Escreva um algoritmo que lê um nome e uma idade
 caso o nome digitado seja Jhonatan, escreva isso na tela
 caso o usuário digite qualquer outro nome, verifique sua idade.
 Se for menor que 18 anos, informe que é menor. Se for maior que 100 anos,
 informe que esta pessoa possivelmente não existe
"""

nome = input('Qual seu nome ?')
idade = int(input('Qual sua idade ?'))
if nome == 'Jhonatan':
    print('Olá, Jhonatan!')
elif idade < 18:
    print('Você não é o Jhonatan! E é menor de idade!')
elif idade > 100:
    print ('Está acima da idade !')
elif idade >= 18 or idade <= 100:
    print('Seja bem vindo!')
