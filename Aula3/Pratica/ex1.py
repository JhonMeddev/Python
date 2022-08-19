"""
Expressões booleanas

- Escreva as Seguintes expressões booleanas em liguagem Python:
a)O somatorio de 2 com 2 é menor do que 4
b)O valor 7 // 3 é igual a 1 + 1 , OBS: // -> parte inteira da divisão
c)A soma de 3 elevado ao quadrado com 4 elevado ao quadrado é igual a 25
d)A soma de 2,4 e 6 é maior do que 12
"""

a = bool((2 + 2) < 4)
b = bool((7 // 3) == 1 + 1)
c = bool((3**2) + (4**2) == 25)
d = bool((2 + 4 + 6) > 12)

print(a)
print(b)
print(c)
print(d)