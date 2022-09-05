"""
Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma pizzaria.
Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
A Pizzaria possui seguinte tabela de sabores de pizzas listados com sua descrição, códigos e valores:

| Código | Descrição | Pizza Média - M | Pizza Grande – G (30% mais cara) |
21        Napolitana       R$ 20,00               R$ 26,00
22        Margherita       R$ 20,00               R$ 26,00
23        Calabresa        R$ 25,00               R$ 32,50
24        Toscana          R$ 30,00               R$ 39,00
25        Portuguesa       R$ 30,00               R$ 39,00


Elabore um programa em Python que:
1.Entre com o tamanho da pizza
2.Entre com o código do produto desejado;
3.Pergunte se o cliente quer pedir mais alguma coisa (se sim repetir a partir do item 1.  Caso contrário ir para próximo passo);
4.Encerre a conta do cliente com o valor total;
5.Deve-se utilizar estruturas if, elif e else (EXIGÊNCIA 1 de 3);
6.Se a pessoa digitar um TAMANHO de pizza e/ou   NÚMERO diferente dos da tabela printar na tela:
‘opção inválida’ e voltar para o menu (EXIGÊNCIA 2 de 3);
7.Deve-se utilizar while, break, continue (EXIGÊNCIA 3 de 3);
(DICA: utilizar o continue dentro else que verifica a opção inválida)
(DICA: utilizar o break dentro if que verifica a opção sair)
8.Colocar um exemplo de SAIDA DE CONSOLE com duas pizzas
9.Colocar um exemplo de SAIDA DE CONSOLE com erro ao digitar código

"""

print("Bem-Vindo a Pizzaria do Jhonatan Medeiros")
#Cardápio
print('=====================Cardápio do dia=====================')
print('| Código | | Descrição | | Pizza Média | | Pizza Grande |')
print('|   21   | |Napolitana | |   R$20,00   | |    R$26,00   |')
print('|   22   | |Margherita | |   R$20,00   | |    R$26,00   |')
print('|   23   | |Calabresa  | |   R$25,00   | |    R$32,50   |')
print('|   24   | |Toscana    | |   R$30,00   | |    R$39,00   |')
print('|   25   | |Portuguesa | |   R$30,00   | |    R$39,00   |')
print('=========================================================')

#Menu Pizza Média
M={
  '21':['Napolitana',20.00],
  '22':['Margherita',20.00],
  '23':['Calabresa',25.00],
  '24':['Toscana',30.00],
  '25':['Portuguesa',30.00]
}

#Menu Pizza Grande
G={
  '21':['Napolitana',26.00],
  '22':['Margherita',26.00],
  '23':['Calabresa',32.50],
  '24':['Toscana',39.00],
  '25':['Portuguesa',39.00]
}

#Variavel do valor
valor=0

#Escolha de Tamanho
while True:
    tamanho=input('Qual tamanho da pizza deseja(M/G)?')
#Tamanho Médio
    if tamanho==('M'):
      #Escolha do código
      codigo=int(input('Qual o código da pizza que deseja?'))

      if codigo==21:
       valor=valor+M['21'][1]
       print('Você pediu uma pizza {}'.format(M['21'][0]))

      elif codigo==22:
       valor=valor+M['22'][1]
       print('Você pediu uma pizza {}'.format(M['22'][0]))

      elif codigo==23:
       valor=valor+M['23'][1]
       print('Você pediu uma pizza {}'.format(M['23'][0]))

      elif codigo==24:
       valor=valor+M['24'][1]
       print('Você pediu uma pizza {}'.format(M['24'][0]))

      elif codigo==25:
       valor=valor+M['25'][1]
       print('Você pediu uma pizza {}'.format(M['25'][0]))

      else:
       print('Código de pizza inválida, escolha novamente.')
       continue

      #Novo Pedido
      novo_pedido_m=input('Deseja fazer outro pedido(S/N)?')

      if novo_pedido_m==('S'):
        continue

      elif novo_pedido_m==('N'):
       print('O total a ser pago é: R${:.2f}'.format(valor))
       break

      else:
       print('Resposta Invalida')
       continue

#Tamanho Grande
    elif tamanho==('G'):
      #Escolha do código
      codigo=int(input('Qual o código da pizza que deseja?'))

      if codigo==21:
       valor=valor+G['21'][1]
       print('Você pediu uma pizza de {}'.format(G['21'][0]))

      elif codigo==22:
        valor=valor+G['22'][1]
        print('Você pediu uma pizza de {}'.format(G['22'][0]))

      elif codigo==23:
        valor=valor+G['23'][1]
        print('Você pediu uma pizza de {}'.format(G['23'][0]))

      elif codigo==24:
        valor=valor+G['24'][1]
        print('Você pediu uma pizza de {}'.format(G['24'][0]))

      elif codigo==25:
        valor=valor+G['25'][1]
        print('Você pediu uma pizza de {}'.format(G['25'][0]))

      else:
        print('Código de pizza inválida, escolha novamente.')
        continue

#Novo Pedido
      novo_pedido_g=input('Deseja fazer outro pedido(S/N)?')

      if novo_pedido_g==('S'):
       continue

      elif novo_pedido_g==('N'):
       print('O total a ser pago é: R${:.2f}'.format(valor))
       break

      else:
       print('Resposta Invalida')
       continue

    else:
      print('Tamanho de pizza invalida,escolha novamente')
      continue