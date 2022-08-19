"""
Escreva um programa que calcule o preço a
pagar pelo fornecimento de energia elétrica.
Pergunte a quantidade de kWh consumida e o tipo de instalção:
R para residência, I para industria e C para comércios

Calcule o preço de acordo com a tabela a seguir:
-------Preço por tipo e faixa de consumo--------
______________________________________
|Tipo      |Faixa(kWh)    |Preço(R$) |
--------------------------------------
Residencial| até 500      | 0,40     |
           | acima de 500 | 0,65     |
--------------------------------------
Comercial  |até 1000       |0,55      |
           |acima de 1000 |0,60      |
--------------------------------------
Industrial |até 5000      |0,55      |
           |acima de 5000 |0,60      |
--------------------------------------
"""

print("---Calculo de energia---")
print("Tipo de Instalação: Residencial(R), Comercial(C) e Industrial(I)")
tipo = input("Digite apenas a letra Referente a instalação R, C ou I : ")
faixa = float(input("Digite a quantidade gasta em kWh: "))

if(tipo == "R"):
    if(faixa <= 500):
        calc = faixa * 0.40
    else:
        calc = faixa * 0.65

elif(tipo == "C"):
    if(faixa <= 1000):
        calc = faixa * 0.40
    else:
        calc = faixa * 0.65
elif(tipo == "I"):
    if(faixa <= 5000):
        calc = faixa * 0.40
    else:
        calc = faixa * 0.65
else:
    print("Tipo de instalação Inválido!")
print("Valor a ser pago : R${}".format(calc))