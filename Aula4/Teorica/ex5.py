"""
Exercício
- Escreva um algoritmo que realize um login em um sistema
- O Usuário deve informa seu nome e senha
"""

print("Digite o login e senha")
while True:
    login = input("Digite o Login : ")
    senha = input("Digite a Senha: ")
    if login == "adm" and senha == "adm":
        print("Logado com sucesso !")
        break
    else:
        print("Login ou senha incorretos")
        continue