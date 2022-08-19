"""
 - Faça um algoritmo que receba três valores,
 representando os lados de um triângulo fornecidos pelo usuário. Verifique se
 os valores forma um triângulo e classifique como:
 a)Equilátero(três lados iguais)
 b)Isósceles(dois lados iguais)
 c)Escaleno(três lados diferentes)

 OBS: Lembre-se de que, para formar um triângulo,
 nenhum dos lados pode ser igual a zero, e um lado
 não pode ser maior do que a soma dos outros dois(exercício da apostila - aula 3)
"""

L1 = int(input("Digite o 1ª lado do triângulo"))
L2 = int(input("Digite o 2ª lado do triângulo"))
L3 = int(input("Digite o 3ª lado do triângulo"))

if (L1 > 0) and (L2 > 0) and (L3 > 0):
    if (L1 + L2 > L3) and (L1 + L3 > L2) and (L2 + L3 > L1):
        if L1 == L2 and L1 == L3:
          print("Triângulo Equilátero")
        elif L1 == L2 or L1 == L3 or L2 == L3:
          print("Triângulo Isósceles")
        elif L1 != L2 or L1 != L3 or L2 != L3:
          print("Triângulo Escaleno")
    else:
        print("um lado não pode ser maior do que a soma dos outros dois")
else:
    print("Nenhum dos lados pode ser zero!")

