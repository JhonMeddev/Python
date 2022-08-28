"""
- Um cinema cobra preço diferentes para os ingressos de
acordo com a idade de uma pessoa. Se a pessoa tiver menos de
3 anos de idade, o ingresso seŕa gratuito,se tive entre
3 e 12 anos, o ingresso custará R$15, se tiver mais de 12 anos,
custará R$30

-Escreva um laço em que você pergunte a idade aos usuários e,
então, informe-lhes o preço do ingresso do cinema

-Encerre o laço usando break quando o usuário digitar sair

-Após encerrar o laço, apresente na tela o total de pessoas que
compraram ingressos, o total de dinheiro arrecadados e a média de idade
das pessoas.
"""

total = 0
dinheiro = 0
somaIdade = 0
while True:
    idade = input("Qual a sua idade ?")
    if idade == "sair":
        break
    idade = int(idade)
    total = total + 1
    somaIdade = idade + idade


    if idade < 3 :
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15
    dinheiro = dinheiro + ingresso
    media = somaIdade / total

print("Total de pessoas: {}".format(total))
print("Total arrecadado: R${}".format(dinheiro))
print("Média de idade das pessoas: {}".format(media))