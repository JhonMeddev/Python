"""
-Escreva uma rotina que crie uma borda ao redor
de uma palavra para destacá-la como sendo um título.
A rotina deve receber como parâmetro a palavra a ser destacada.
O tamanha da caixa de texto deverá ser adaptável de acordo com
tamano da palavra. Por exemplo:
+--------+      +---+
|Jhonatan|      |Olá|
+--------+      +---+
"""

#Função:
def borda(s1):
    tam = len(s1)
    #Só imprime caso exista algum caractere
    if tam:
        print('+','-' * tam, '+')
        print('|', s1,'|')
        print('+','-'*tam,'+')
#Programa Principal:
borda('Olá, Mundo!')
borda('Lógica de Programação e Algoritmos')