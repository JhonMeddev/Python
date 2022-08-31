"""
-Imagine uma situação na qual você deve realizar o cadastro
de uma lista de compras em um sistema. Caada produto comprado
deverá ser registrado com seu nome, quantidade e valor unitário

"""

item = []
mercado = []

for i in range(3):
    item.append(input('Digite o nome do item: '))
    item.append(int(input('Digite a quantidade: ')))
    item.append(float(input('Digite o valor: ')))
    mercado.append(item[:])
    item.clear()
print(mercado)