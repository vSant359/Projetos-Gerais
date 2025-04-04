import json
import random

try:
    with open('Projetos-Gerais/akinator/dados.json', 'r') as file:
        dados = json.load(file)
except FileNotFoundError:
    print("Arquivo não encontrado!")
    exit()
except json.JSONDecodeError:
    print("Erro ao decodificar o arquivo JSON!")
    exit()


certo = []
errado = []

def main():
    print("Olá, sou uma cópia feita em casa do akinator, \n escolha um entre esses artistas e eu lerei sua mente: ")
    
    for celebridades in dados:
        print(celebridades["nome"])
    input("Precione enter para continuar...")
    escolher_pergunta()


def gerar_pergunta(item):
    tentativas = 0  # Contador para limitar tentativas
    while tentativas < 100:  # Limite de 100 tentativas
        while True:
            artista = random.choice(dados)  
            atributos = artista["filmes"] + artista["premios"] + artista["outros"]
            if any(item in errado for item in atributos):
                continue
            
            filme = random.choice(artista[item])  
            
            if filme in errado:  
                continue
            elif filme in certo:  
                outras_chaves = [chave for chave in artista if chave != item]
                if outras_chaves:
                    novo_item = random.choice(outras_chaves)
                    return random.choice(artista[novo_item])
        
            return filme


def pergunta_filme():
    filme = gerar_pergunta("filmes")
    print(f"A pessoa escolhida participou de {filme}? ")
    print("Escolha uma opção:")
    print("1 - Sim")
    print("2 - Não")
    print("3 - Não sei")
    resposta = input("Digite o número da sua escolha: ")
    while resposta not in ['1', '2', '3']:
        resposta = input("Opção inválida! Digite 1, 2 ou 3: ")
    if resposta == "1":
        certo.append(filme)
        print(certo)
    elif resposta == "2":
        errado.append(filme)
    elif resposta == "3":
        pass
    verificar_respostas()
    escolher_pergunta()


def pergunta_premio():
    premio = gerar_pergunta("premios")
    print(f"A pessoa escolhida já ganhou o {premio}?")
    print("Escolha uma opção:")
    print("1 - Sim")
    print("2 - Não")
    print("3 - Não sei")
    resposta = input("Digite o número da sua escolha: ")
    while resposta not in ['1', '2', '3']:
        resposta = input("Opção inválida! Digite 1, 2 ou 3: ")
    if resposta == "1":
        certo.append(premio)
        print(certo)
    elif resposta == "2":
        errado.append(premio)
    elif resposta == "3":
        pass
    verificar_respostas()
    escolher_pergunta()


def pergunta_outros():
    outro = gerar_pergunta("outros")
    print(f"A pessoa escolhida é um(a) {outro}? ")
    print("Escolha uma opção:")
    print("1 - Sim")
    print("2 - Não")
    print("3 - Não sei")
    resposta = input("Digite o número da sua escolha: ")
    while resposta not in ['1', '2', '3']:
        resposta = input("Opção inválida! Digite 1, 2 ou 3: ")
    if resposta == "1":
        certo.append(outro)
        print(certo)
    elif resposta == "2":
        errado.append(outro)
    elif resposta == "3":
        pass
    verificar_respostas()
    escolher_pergunta()

def verificar_respostas():
    """Verifica se há um artista que contém todas as respostas positivas"""
    candidatos = []
    
    for artista in dados:
        atributos = artista["filmes"] + artista["premios"] + artista["outros"]
        if any(item in errado for item in atributos):
            continue

        if all(item in atributos for item in certo):
            candidatos.append(artista["nome"])

    if len(candidatos) == 1:
        print(f"Eu acho que é {candidatos[0]}, estou certo?")
        print("Escolha uma opção:")
        print("1 - Sim")
        print("2 - Não")
        resposta = input("Digite o número da sua escolha: ")
        while resposta not in ['1', '2']:
            resposta = input("Opção inválida! Digite 1 ou 2: ")
        if resposta == "1":
                print(f"Entao é isso a pessoa que você pensou é {candidatos[0]}, eu li sua mente!")
                exit()
        else:
            print("Ok, vamos tentar de novo...")
            escolher_pergunta()
    elif len(candidatos) == 0:
        print("Hmmm... parece que os dados não batem com ninguém. Você me venceu, gostaria de jogar novamente?.")
        print("Escolha uma opção:")
        print("1 - Sim")
        print("2 - Não")
        resposta = input("Digite o número da sua escolha: ")
        while resposta not in ['1', '2']:
            resposta = input("Opção inválida! Digite 1 ou 2: ")
        if resposta == "1":
            certo.clear()
            errado.clear()
            main()

    else:
        print(f"Ainda restam {len(candidatos)} possibilidades...")






def escolher_pergunta():
    funcoes = [pergunta_filme, pergunta_premio, pergunta_outros]
    random.choice(funcoes)()


if __name__ == '__main__':
    main()