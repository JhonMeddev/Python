"""
   Condicional composta
- Traduza as afirmações a seguir para condicionais em Python:
a) Se ano é divisível por 4, escreva: "Pode ser um ano bissexto".
Caso contrario, escreva: "Definitivamente não é um ano bissexto"

b)Se ambas as variaveis booleana cima e baixo forem True, escreva: "Decida-se!",
caso contrario, escreva: "Você escolheu um caminho!"
"""

# a
ano = 2022
if (ano % 4 == 0):
    print("Pode ser um ano bissexto")
else:
    print("Definitivamente não é um ano bissexto")

# b

cima: bool = True
baixo: bool = False
if (cima == True and baixo == True):
    print("Decidade-se!")
else:
    print("Você escolheu um caminho!")