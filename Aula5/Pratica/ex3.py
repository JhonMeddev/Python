"""
-Suponha que você é um colecionador de jogos de videogame. Escreva
um algoritmo que premita cadastrar eses jogos informando o nome e
a qual videogame ele pertence

- Para isso, crie um menu de opções contendo:
cadastrar novo item, listar tudo que foi cadastrado e sair

-Para resolver este exercício, crie pelo menos uma função
para cada item do menu
-Além disso, armazene todos os dados em um arquivo de texto que deve
ser salvo em disco e manter os dados cadastrados
"""

def validacao(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def criaArquivo(nomeArquivo):
    try:
        # w = abrir arquivo para escrita, t = arquivo do tipo txt
        # + = caso não exista o arquivo ele cria
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nomeArquivo))


def existeArquivo(nomeArquivo):
    try:
        # r = abrir arquivo para leitura e t = abrir arquivo txt
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def listarArquivo(nomeAquivo):
    try:
        # r = somente leitura
        # t = arquivo txt
        a = open(nomeAquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        # a = Escrita, mas preserva o conteúdo se já existir
        # t = arquivo txt
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{};{}\n'.format(nomeJogo, nomeVideogame))
    finally:
        a.close()



#Programa principal
arquivo = 'ex3Games.txt'

if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)

while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - Sair')

    op = validacao('Escolha a opção desejada: ',1, 3)
    if op == 1:
        print('Opção de cadastrar novo item selecionada ... \n')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)

    elif op == 2:
        print('Opção de listar selecionada ... \n')
        listarArquivo(arquivo)

    elif op == 3:
        print("Encerrando o programa...")
        break