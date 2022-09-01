"""
- Dada uma lista contendo as notas de alunos em uma disciplina,
escreva uma expressão para:
   notas = [9,7,7,10,3,9,6,6,2]
 a) Encontrar quantos alunos tiraram nota 7
 b) Alterar a útima nota para 4
 c) Encontrar a maior nota
 d) Ordenar a lista de notas
 e) A média das notas
"""

# a) Encontrar quantos alunos tiraram nota 7
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

print("Quantidade de alunos que tiraram nota 7 = {}".format(notas.count(7)))

# b) Alterar a útima nota para 4
notas[-1] = 4
print(notas)

# c) Encontrar a maior nota
print(max(notas))

# d) Ordenar a lista de notas
notas.sort()
print(notas)

# e) A média das notas
somaNotas = sum(notas)
media = somaNotas / 9
print("A média das notas é de : {}".format(media))