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
    def _init_(self, cadastro, nome, historico = None):
        self.cadastro = cadastro
        self.nome = nome
        self.historico = historico # provavelmente funcionará bem com dicionário


class Biblioteca():
    estante = []
    def init (self):
        self.catalogo_livros = []
        self.registro_membros = []

    def adicionar_estante(self, item):
        self.estante.append(item)
        return self.estante

    # def estante_livros (self):
    #     if len(self.estante) == 0:
    #         id = 1
    #     else:
    #         id = self.estante[-1]
    #     return id

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
        cadastro = 1
        membro = Membro (cadastro, nome)
        Membro.membros.append(membro)
        main()
        
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
            main()

    def pesquisando_nome (self, livro): 
        for item in Biblioteca.estante: 
            if item['titulo'] == livro:
                print(f"0 livro {item['titulo']} está {item['status']}")
                main()
        
    
    def pesquisando_autor(self, autor):
        print(f'Vamos ver os livros de {autor}...')
        for item in Biblioteca.estante:
            if item['autor'] == autor:
                print(f'Livro: {item["titulo"]}, autor: {item["autor"]}, status: {item["status"]}')
            if item['autor'] != autor:
                print('Livro não encontrado')
                main()
        

def emprestar(self):
    pass

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

if __name__ == '__main__':
    main()