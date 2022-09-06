"""
Imagina-se que você e sua equipe foram contratados por um restaurante que serve feijoada para
desenvolver a solução de software. Você ficou encarregado da parte de retirar pedido por parte do cliente.
O valor que a empresa cobra por feijoada é dado pela seguinte equação:
total=(volume*opção)+adional(is)
Em que cada uma das variáveis que compõe o preço total é quantizada da seguinte maneira:

Quadro 1: Volume versus Valor
volume (ml)              |      valor (R$)     |
 volume < 300            |     Não é aceito    |
300  <= volume <= 5000   |     volume * 0.08   |
volume > 5000            |    Não é aceito     |




Quadro 2: Opção versus multiplicador
peso(kg)                                 |  multiplicador
b - Básica (Feijão + paiol + costelinha)       1.00
p - Premium (Feijão + paiol + costelinha
 + partes de porco)                            1.25
s - Suprema (Feijão + paiol + costelinha
 + partes do porco + charque + calabresa
 + bacon)                                      1.50




Quadro 3: Acompanhamento versus Valor
rota                                                 | Valor (R$)
0- Não desejo mais acompanhamentos (encerrar pedido) |   0,00
1- 200g de arroz                                     |   5,00
2- 150g de farofa especial                           |   6,00
3- 100g de couve cozida                              |   7,00
4- 1 laranja descascada                              |   3,00


Elabore um programa em Python que:
1.Pergunte o volume (em ml).Se digitar um valor não numérico e/ou volume for menor/maior que o limite aceito repetir a pergunta;
2.Pergunte a opção da feijoada. Se digitar uma opção não válida deve repetir a pergunta
3.Pergunte o acompanhamento. Deve-se perguntar se o usuário quer mais um acompanhamento até digitar a opção 0
4.Encerre o total a ser pago com base na equação desse enunciado;
5.Deve-se codificar uma função volumeFeijoada (EXIGÊNCIA 1 de 3);
    Deve-se perguntar dentro da função o volume da porção (em ml);
    Deve-se ter um if/else ou if/elif ou if/else/elif para verificar se o usuário não digitou um volume fora da faixa com que o restaurante trabalha;
    Deve-se ter try/except para o caso do usuário digitar um valor não numérico;
    Deve-se retornar o valor em (RS) conforme a Quadro 1
6.Deve-se codificar uma função opcaoFeijoada (EXIGÊNCIA 2 de 3);
    Deve-se perguntar dentro da função a opção desejada;
    Deve-se ter um if/elif/else para verificar as opções possíveis ou não;
    Deve-se retornar o multiplicador conforme o Quadro 2
7.Deve-se codificar uma função acompanhamentoFeijoada (EXIGÊNCIA 3 de 3);
    Deve-se perguntar dentro se deseja ou não mais algum acompanhamento
    Deve-se ter um if/elif/else para verificar as opções possíveis ou não;
    Deve-se retornar o multiplicador conforme o Quadro 3
8.Colocar um exemplo de SAIDA DE CONSOLE um pedido com volume, opção e 2 acompanhamentos válidos
9.Colocar um exemplo de SAIDA DE CONSOLE com o tratamento de erro quando digitado um valor não numérico é digitado e uma opção não permitida no menu opção de feijoada

"""

# identificador pessoal
print(f"Bem vindo a loja do Jhonatan Medeiros")

# INICIO DO CÓDIGO PRINCIPAL
opcoes = {
   "b": ["Básica (Feijão + Paiol + Costelinha)", 1],
   "p": ["Premium (Feijão + Paiol + Costelinha + Partes de porco)", 1.25],
   "s": ["Suprema (Feijão + Paiol + Costelinha + Partes do porco + Charque + Calabresa + Bacon)", 1.50]
}

acompanhamentos = {
   0: ["Não quero mais acompanhamentos (encerrar pedido)", 0],
   1: ["200g de arroz", 5],
   2: ["150g de farofa especial", 6],
   3: ["100g de couve cozida", 7],
   4: ["1 laranja descascada", 3]
}

# Função que solicita e valida o volume
def volume():
   valor = 0
   while True:
       try:
           volume = float(input("Entre com a quantidade que deseja (ml): ").strip().upper())
           if volume < 300 or volume > 5000:
               print("Não aceitamos porções menores que 300ml ou maiores que 5L.Tente novamente!")
           else:
               valor = volume * 0.08
               break
       except ValueError:
           print("Digite um volume válido.")
   return valor

 # Função que solicita e valida a opção
def opcaoFeijoada():
   multiplicador = None
   while True:
       try:
           print("Entre com a opção de Feijoada:")
           for key, values in opcoes.items():
               print(f"{key} - {values[0]}")
           opcao = input().strip().lower()

           if opcao not in opcoes.keys():
               print("Opção inválida")

           else:
               multiplicador = opcoes[opcao][1]
               break

       except ValueError:
           print("Digite um opcao válida.")

   return multiplicador

# Função que solicita e valida os acompanhamentos
def acompanhamentoFeijoada():
   total_acompanhamento = 0

   while True:
       try:
           print("Deseja mais algum acompanhamento:")

           for key, values in acompanhamentos.items():
               print(f"{key} - {values[0]}")

           opcao = int(input())

           if opcao not in acompanhamentos.keys():
               print("Opção inválida")

           elif opcao == 0:
               break

           else:
               total_acompanhamento += acompanhamentos[opcao][1]

       except ValueError:
           print("Digite um acompanhamento válido.")

   return total_acompanhamento

valor = volume()

opcao = opcaoFeijoada()

adicionais = acompanhamentoFeijoada()

total = (valor * opcao) + adicionais

print(f"O valor total a ser pago pelo seu pedido é de (R$): {total:.2f} (Volume = {valor:.2f} * opcao = {opcao:.2f} + Acompanhamento = {adicionais:.2f})")