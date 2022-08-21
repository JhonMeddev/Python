"""
-Escreva um algoritmo que fique recebendo frases ou
palavras digitadas pelo usuário

Encerre o algoritmo quando a palavra
sair for digitada
"""

print('Digite uma mensagem que irei repetir para você!')
print("Para encerrar digite 'sair'.")
while True:
    texto = input('')
    if texto == "sair":
        break
    print(texto)
print('Encerrando programa ...')