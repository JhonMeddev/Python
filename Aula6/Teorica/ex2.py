"""
-Imagine uma situação na qual você deve realizar o cadastro
de uma lista de compras em um sistema. Caada produto comprado
deverá ser registrado com seu nome, quantidade e valor unitário

"""

mercado = []

for i in range(3):
    nome = input("Digite o nome do item: ")
    qtd = int(input('Digite a quantidade: '))
    valor = float(input('Digite o valor: '))
    mercado.append([nome, qtd, valor])
print(mercado)

#Print e soma da lista de compras

soma = 0
print('Lista de compras:')
print('-' * 20)
print('Item | quantidade | valor unitário | total do item')
for item in mercado:
    print('{} | {} | {} | {}'.format(item[0], item[1], item[2], item[1] * item[2]))
    soma += item[1] * item[2]
print('-' * 20)
print('Total a ser pago: {}'.format(soma))