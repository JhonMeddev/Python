"""
Imagina-se que você é um dos programadores responsáveis pela construção
de app de vendas para uma determinada empresa X que vende em atacado.
Uma das estratégias de vendas dessa empresa X é dar desconto maiores por unidade conforme a tabela abaixo:
Quantidades
Desconto
Até 4
0% na unidade
Entre 5 e 19
3% na unidade
Entre 20 e 99
6% na unidade
Maior ou igual a 100
10% na unidade

Elabore um programa em Python que:
1.Entre com o valor unitário do produto (Lembrar que número decimal é feito com ponto e não vírgula);
2.Entre com a quantidade desse produto;
3.O programa deve retornar o valor total sem desconto;
4.O programa deve retornar o valor total após o desconto;
5.Deve-se utilizar estruturas if, elif e else (EXIGÊNCIA 1 de 1);
6.Colocar um exemplo de SAIDA DE CONSOLE de compra de mais de 10 und.

"""


print("Bem vindo a Loja do Jhonatan Medeiros")
#Pegando valor e quantidade do usuario
valor = float(input("Entre com valor do produto: "))
qtd = int(input("Entre com valor do quantidade: "))

#Definindo qual será o desconto com base na qtd
if 0 <= qtd < 4:
    desconto = 0
    print("O valor com desconto foi: R$ {}".format(desconto))
elif 5 <= qtd < 20:
    desconto = 0.03
elif 20 <= qtd < 100:
    desconto = 0.06
else:
    desconto = 0.1

#Calculos
semDesconto = valor * qtd
comDesconto = semDesconto - (semDesconto * desconto)
print("O valor sem desconto foi : R$ {:.2f}".format(semDesconto))
print("O valor com desconto foi : R$ {:.2f}  (desconto {:.0%})".format(comDesconto, desconto))