"""
- Escreva um algoritmo que crie uma tupla com
10 palavras. Encontre dentro dessa tupla as
vogais de cada palavra. Faça um print na tela
com o nome da palavra e suas respectivas
vogais

"""

tupla = ('Filosofia', 'Ciência', 'Cosmo', 'Universo', 'Etimologia',
         'Gnose', 'Egito', 'Grecia', 'Liberdade', 'Pensamento')

#Varrredura na tupla com For
for palavra in tupla:
    print('\nPalavra: {}. Vogais: '.format(palavra.upper()), end='')
    #indexação dupla para verfificar se é vogal
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')