"""
While x for
Realize a sequência de print com for e while:
a) Inteiros de 3 até 12, com 12 inluso
b)Inteiros de 0 até 9, excluido 9, com passo de 2
"""

#LAÇO DE REPETIÇÃO COM FOR exercicio "a"
#for i in range (3, 13, 1): OU
for i in range (3, 13):
    print("For exercicio a: {}".format(i))

#LAÇO DE REPETIÇÃO COM WHILE exercicio "a"
n = 3
while(n < 13 ):
    print("While exercicio a: {} ".format(n))
    n = n + 1

#LAÇO DE REPETIÇÃO COM FOR exercicio "b"
for b in range (0, 9, 2):
    print("For exercicio b: {}".format(b))

#LAÇO DE REPETIÇÃO COM WHILE exercicio "b"
c = 0
while (c < 9):
    print("While exercicio b: {}".format(c))
    c = c + 2