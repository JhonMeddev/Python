"""
-----Validando dados de entreada
Exemplo:
-Crie um algoritmo que receba um valor do tipo inteiro via teclado
-No entanto, o programa só deve aceitar, obrigatoriamente,
valores inteiros e positivos
-Qualquer valor negativo, ou igual a zero, deve ser rejeitado pelo
programa e um novo valor deve ser solicitado
"""

valor = int(input("Digite apenas valores inteiros e positivos: "))
while valor % 2 != 0:
    valor = int(input("Digite um valor positivo! : "))
print("Obrigado, o valor {} é valido !".format(valor))