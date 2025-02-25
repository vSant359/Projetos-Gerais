import json
import random

with open('akinator\\dados.json', 'r') as file:
    dados = json.load(file)

certo = []
errado = []

def main():
    print("Olá, sou uma cópia feita em casa do akinator, \n escolha um entre esses artistas e eu lerei sua mente: ")
    
    for celebridades in dados:
        print(celebridades["nome"])
    input("Precione enter para continuar...")
    escolher_pergunta()


def gerar_pergunta(item, artista):
    while True:
        if item in artista and item in errado:
            continue
        if item in artista and item in certo:
            opcoes = [chave for chave in artista.keys() if chave != item]
            if not opcoes:
                continue
            item = random.choice(opcoes)
        
        return random.choice(artista[item])


def pergunta_filme():
    artista = random.choice(dados)
    filme = gerar_pergunta("filmes", artista)
    resposta = input(f"A pessoa escolhida participou de {filme}? (s/n/nsei)")
    if resposta == "s":
        certo.append(filme)
        print(certo)
    elif resposta == "n":
        errado.append(filme)
    elif resposta == "nsei":
        pass
    verificar_respostas()
    escolher_pergunta()


def pergunta_premio():
    artista = random.choice(dados)
    premio = gerar_pergunta(artista, "premios")
    resposta = input(f"A pessoa escolhida já ganhou o {premio}? (s/n/nsei)")
    if resposta == "s":
        certo.append(premio)
        print(certo)
    elif resposta == "n":
        errado.append(premio)
    elif resposta == "nsei":
        pass
    verificar_respostas()
    escolher_pergunta()


def pergunta_outros():
    artista = random.choice(dados)
    outro = gerar_pergunta(artista, "outros")
    resposta = input(f"A pessoa escolhida é um(a) {outro}? (s/n/nsei)")
    if resposta == "s":
        certo.append(outro)
        print(certo)
    elif resposta == "n":
        errado.append(outro)
    elif resposta == "nsei":
        pass
    verificar_respostas()
    escolher_pergunta()

def verificar_respostas():
    """Verifica se há um artista que contém todas as respostas positivas"""
    candidatos = []
    
    for artista in dados:
        if artista not in errado:  
            atributos = artista["filmes"] + artista["premios"] + artista["outros"]
        
        if all(item in atributos for item in certo):
            candidatos.append(artista["nome"])

    if len(candidatos) == 1:
        print(f"Eu adivinhei! A pessoa escolhida é {candidatos[0]}!")
        exit()
    elif len(candidatos) == 0:
        print("Hmmm... parece que os dados não batem com ninguém. Vamos continuar.")
    else:
        print(f"Ainda restam {len(candidatos)} possibilidades...")






def escolher_pergunta():
    funcoes = [pergunta_filme, pergunta_premio, pergunta_outros]
    random.choice(funcoes)()


if __name__ == '__main__':
    main()