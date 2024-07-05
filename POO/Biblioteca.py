class Livro():
    def __init__(self, id, titulo, autor, status):
        pass
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.status = status

    def ver_livros (self):
        novo_livro = []
        for item in Biblioteca.estante:
            novo_livro.append(str(item))
            print(novo_livro[-1])
        return novo_livro


class Membro():
    membros = []
    def __init__(self, cadastro, nome, historico = None):
        pass
        self.cadastro = cadastro
        self.nome = nome
        self.historico = historico # provavelmente funcionará bem com dicionário

    def ver_membros (self):
        novo_membro = []
        for item in Membro.membros:
            novo_membro.append(str(item))
            print(novo_membro[-1])
        return novo_membro


class Biblioteca():
    estante = []
    def init (self):
        self.catalogo_livros = []
        self.registro_membros = []

    def adicionar_estante(self, item):
        self.estante.append(item)
        return self.estante


    def adicionando_status():
        status_livro = input('Digite emprestado ou em estoque para definir o status do livro: ')
        if status_livro == 'em estoque':
            status = True
        else: #Fazer validacão            
            status = False
        return status_livro

    def adicionar_catalogo(self): 
        print('Adicionando livro')
        id = len(self.estante)
        titulo = input('Adicione o título do livro: ')
        autor = input('Adicione o autor do livro: ')
        status = self.adicionando_status()
        livro = Livro(id, titulo, autor, status)
        Biblioteca.estante.append(livro.__dict__)
        livro.ver_livros()
        main()

    def cadastrar_membros(self):
        nome = input('Digite aqui o nome do novo membro: ')
        cadastro = len(Membro.membros)
        membro = Membro (cadastro, nome)
        Membro.membros.append(membro.__dict__)
        Membro.ver_membros(Membro)
        main()

    def pesquisando_nome(self, livro_escolhido): 
            for livro in Biblioteca.estante: 
                if livro['titulo'] == livro_escolhido:
                    print(f"0 livro {livro['titulo']} está {livro['status']}")
            return livro
          
        
    
    def pesquisando_autor(self, autor_escolhido):
        print(f'Vamos ver os livros de {autor_escolhido}...')
        for autor in Biblioteca.estante:
            if autor['autor'] == autor_escolhido:
                print(f'Livro: {autor["titulo"]}, autor: {autor["autor"]}, status: {autor["status"]}')
            if autor['autor'] != autor_escolhido:
                print('Livro não encontrado')
        return autor
            
        
    def pesquisando_id(self):
        id_escolhido = int(input("Digite aqui o id do liro: "))
        for id in Biblioteca.estante:
            if id['id'] == id_escolhido:
                print(f'O id {id["id"]} é referente ao livro {id["titulo"]} e seu status é {id["status"]}')
            if id['id'] != id_escolhido:
                print('Livro não encontrado')
        return id["titulo"]

    def pesquisando_membro(self, membro_escolhido):
        for membro in Membro.membros:
            if membro['nome'] == membro_escolhido:
                print(f'Seu nome é {membro["nome"]} seu numero de cadastro é {membro["cadastro"]} e seu histórico é {membro["historico"]}')
            if membro['nome'] != membro_escolhido:
                print('Membro não encontrado')
        return membro
        
    def pesquisar(self):
        print('Como você gostaria de pesquisar seu livro?')
        print('1) Pelo nome do livro')
        print('2) Pelo nome do autor')
        print('3) Pelo id do livro')
        escolha = int(input('Digite o numero da opção desejada: '))
        if escolha == 1:
            titulo = input('Digite o título do livro que está procurando: ')
            self.pesquisando_nome(Biblioteca, titulo)
        elif escolha == 2:
            nome_autor = input('Digite aqui o nome do autor do livro: ')
            self.pesquisando_autor(Biblioteca, nome_autor)

        elif escolha == 3:
            
            self.pesquisando_id(Biblioteca, id)

        resultado_pesquisa = self.pesquisando_nome()
        return resultado_pesquisa
            # main()
        


    def emprestar(self):
      nome_membro = input('Digite aqui seu nome para localizarmos seu cadastro: ')
      self.pesquisando_membro(Biblioteca, nome_membro)
      self.pesquisar(Biblioteca)
      result = self.pesquisar()
      print(result)
      

    def devolucao(self):
        pass

def main():
    print('Olá, o que você deseja fazer?')
    print('1) Adicionar um livro ao catálogo')
    print('2) Cadastrar um novo membro')
    print('3) Pesquisar um livro dentro do catálogo')
    print('4) Emprestar um livro a um membro')
    print('5) Registrar a devolução do livro para a biblioteca')
    escolha = int(input('Digite o número da opção desejada: '))
    if escolha == 1:
        Biblioteca.adicionar_catalogo (Biblioteca)
    elif escolha == 2:
        Biblioteca.cadastrar_membros (Biblioteca)
    elif escolha == 3:
        Biblioteca.pesquisar (Biblioteca)
    elif escolha == 4:
        Biblioteca.emprestar(Biblioteca)

if __name__ == '__main__':
    main()