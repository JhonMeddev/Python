"""
   Condicional simples
-Traduza as afirmações a seguir para condicionais em Python:

a) Se idade é maior que 60, escreva: "Você tem direito aos benefícios"
b)Se dano é maior do que 10 e escudo é igual a 0, escreva "Você está morto!"
c)Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem
em True, escreva: "Você escapou"
"""

# a
idade: int = 70
if (idade > 60):
    print("Você tem direito aos beneficios!")

# b
dano: int = 101
escudo: int = 0
if dano > 10 and escudo == 0:
    print('Você está morto!')

# c
norte: bool = False
sul: bool = True
leste: bool = False
oeste: bool = False

if (norte == True or sul == True or leste == True or oeste == True):
    print("Você escapou!")

