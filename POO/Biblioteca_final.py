import unidecode

# livros = [
#     {"id": 0, "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "status": True},
#     {"id": 1, "titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "status": False},
#     {"id": 2, "titulo": "1984", "autor": "George Orwell", "status": True},
#     {"id": 3, "titulo": "A Revolução dos Bichos", "autor": "George Orwell", "status": False},
#     {"id": 4, "titulo": "Dom Quixote", "autor": "Miguel de Cervantes", "status": True},
#     {"id": 5, "titulo": "Novelas Exemplares", "autor": "Miguel de Cervantes", "status": False},
#     {"id": 6, "titulo": "Orgulho e Preconceito", "autor": "Jane Austen", "status": True},
#     {"id": 7, "titulo": "Razão e Sensibilidade", "autor": "Jane Austen", "status": False},
#     {"id": 8, "titulo": "Guerra e Paz", "autor": "Liev Tolstói", "status": True},
#     {"id": 9, "titulo": "Anna Karenina", "autor": "Liev Tolstói", "status": False}
# ]


# membros = [
#     {"cadastro": 1, "nome": "Ana Silva", "historico": []},
#     {"cadastro": 2, "nome": "Bruno Costa", "historico": []},
#     {"cadastro": 3, "nome": "Carla Souza", "historico": []},
#     {"cadastro": 4, "nome": "Daniel Oliveira", "historico": []},
#     {"cadastro": 5, "nome": "Elena Ferreira", "historico": []},
#     {"cadastro": 6, "nome": "Felipe Santos", "historico": []},
#     {"cadastro": 7, "nome": "Gabriela Pereira", "historico": []},
#     {"cadastro": 8, "nome": "Henrique Lima", "historico": []},
#     {"cadastro": 9, "nome": "Isabel Mendes", "historico": []},
#     {"cadastro": 10, "nome": "João Almeida", "historico": []}
#      ]




class Livro():
    def __init__(self, id, titulo, autor, status):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.status = status

    def __repr__(self):
        return "ID: {}, Título: {}, Autor: {}, Status: {}\n".format(self.id, self.titulo, self.autor, 'em estoque' if self.status else 'emprestado')
        
    
    def adicionar_catalogo(self):
        print('Adicionando livro')
        for item in livros:
            titulo = item['titulo']
            id = item['id']
            autor = item['autor']
            status = item['status']
            livro = Livro(id, titulo, autor, status)
            Biblioteca.estante.append(livro)
        print(Biblioteca.estante)
        main()



class Membro():
    def __init__(self, cadastro, nome, historico):
        self.cadastro = cadastro
        self.nome = nome
        self.historico = []


    def __repr__(self):
        return "Cadastro: {}, Nome: {}, Histórico: {}\n".format(self.cadastro, self.nome, self.historico)
        

    def cadastrar_membros(self):
        for item in membros:
            cadastro = item['cadastro']
            nome = item['nome']
            historico = item['historico']
            membro = Membro (cadastro, nome, historico)
            Biblioteca.nossos_membros.append(membro)
        print(Biblioteca.nossos_membros)
        main()


class Biblioteca():
    estante = []
    nossos_membros = []
    def init (self):
        self.catalogo_livros = []
        self.registro_membros = []

    
    def adicionar_estante(self, item):
        self.estante.append(item)
        return self.estante
    

    def remover(self, item, local):
        if item in local:
            local.remove(item)


    def alterar_status(self, livrin):
        for livro in self.estante:
            if livro.titulo == livrin.titulo:
                if livro.status:
                    livro.status = False
                else:
                    livro.status = True
                return livro
        

    def normalizar_texto(self, texto):
        return unidecode.unidecode(texto.lower())
    
    
    def pesquisar(self, tipo, valor):
        valor_normalizado = self.normalizar_texto(Biblioteca, str(valor))

        campo = 'titulo' if tipo == 1 else 'autor' if tipo == 2 else 'id'

        for livro in self.estante:
            campo_valor_normalizado = self.normalizar_texto(Biblioteca, str(getattr(livro, campo)))
            if campo_valor_normalizado == valor_normalizado:
                return livro
        print(f"Não encontramos nenhum livro com {campo} {valor}.")
        return None
    

    def pesquisar_membro(self, nome_membro):
        for membro in self.nossos_membros:
            if membro.nome == nome_membro:
                print(f"Nome: {membro.nome}, Cadastro: {membro.cadastro}, Histórico: {membro.historico}")
                return membro
        print("Membro não encontrado")
        return None
        

    def iniciar_pesquisa(self):
        print("Como você gostaria de pesquisar seu livro?")
        print("1) Pelo título")
        print("2) Pelo autor")
        print("3) Pelo ID")

        try:
            tipo = int(input("Digite o número da opção desejada: "))
            if tipo not in [1, 2, 3]:
                raise ValueError("Opção inválida")
            
            valor = input("Digite o valor correspondente: ") if tipo != 3 else int(input("Digite o ID do livro: "))
            print(f"Vamos procurar por {valor}")
            resultado = self.pesquisar(Biblioteca, tipo, valor)

            if resultado:
                print(f"O livro {resultado.titulo} de {resultado.autor} está {'em estoque' if resultado.status else 'emprestado'}")
                return resultado
            else:
                self.iniciar_pesquisa(Biblioteca)
            
        except ValueError as e:
            print(e)
            self.iniciar_pesquisa(Biblioteca)


    def emprestar(self):
        try:
            nome_membro = input('Digite aqui seu nome para localizarmos seu cadastro: ')
            result_nome = self.pesquisar_membro(Biblioteca, nome_membro)
            if result_nome:
                controle = False
                while not controle:
                    result = self.iniciar_pesquisa(Biblioteca)
                    if result.status == False:
                        print('Este livro não está disponível, por favor selecione outro livro de sua escolha')
                        print(Biblioteca.estante)
                        continue
                          
                    escolha = int(input(f"{result_nome.nome}, gostaria de pegar o livro {result.titulo} emprestado? (1/2)"))
                    if escolha == 1:
                        final_result = self.alterar_status(Biblioteca, result)
                        result_nome.historico.append(final_result.titulo)
                        print(f"O livro {result.titulo}, foi emprestado.")
                        controle = True
                        main()

        except Exception as e:
            print(f"Ocorreu um erro {e}")
        main()

    
    def devolucao(self):
        print('Para fazer a devolução vamos primeiramente localizar seu cadastro.')
        cliente_nome = input('Digite aqui seu nome: ')
        membro = self.pesquisar_membro(self, cliente_nome)
        print('Agora vamos localizar qual livro você deseja devolver')
        livro = self.iniciar_pesquisa(Biblioteca)
        escolha = input(f"Você gostaria de devolver o livro {livro.titulo}? (s/n) ")
        if escolha == "s":
            atualizacao = self.alterar_status(Biblioteca, livro)
            print(f"Certo, o livro {atualizacao.titulo} foi devolvido a biblioteca, agora ele está {'em estoque' if atualizacao.status else 'emprestado'}")
            main()
        else:
            main()


    def excluir_livro(self):
        livro_escolhido = self.iniciar_pesquisa(Biblioteca)  
        if livro_escolhido:  
            escolha = input(f"Você tem certeza que gostaria de excluir o livro '{livro_escolhido.titulo}' do catálogo? (s/n) ")
            if escolha.lower() == 's':
                self.remover(Biblioteca, livro_escolhido, self.estante)  
                print(f"O livro '{livro_escolhido.titulo}' foi excluído do catálogo.")
                main()
            else:
                print("A exclusão foi cancelada.")
        else:
            print("Não foi possível encontrar o livro para excluir.")
        
    
    def excluir_membro(self):
        nome_membro = input('Digite aqui seu nome para localizarmos seu cadastro: ')
        membro_escolhido = self.pesquisar_membro(Biblioteca, nome_membro)
        if membro_escolhido:
            escolha = input(f"Você tem certeza que gostaria de excluir o cadastro de {membro_escolhido.nome}? (s/n) ")
            if escolha == 's':
                self.remover(Biblioteca, membro_escolhido, self.nossos_membros)
                print(f"O cadastro de {membro_escolhido.nome} foi excluído.")
                main()
            else:
                print("a exclusão foi cancelada.")
                main()
        else:
            print("Não foi possível encontrar o membro para excluir.")


def main():
    
    opcoes = [
        ' Adicionar um livro ao catálogo',
        ' Cadastrar um novo membro',
        ' Pesquisar um livro dentro do catálogo',
        ' Emprestar um livro a um membro',
        ' Registrar a devolução do livro para a biblioteca',
        ' Ver todos os livros na biblioteca',
        ' Ver todos os membros da biblioteca',
        ' Excluir livros da biblioteca',
        ' Excluir membros da biblioteca'
    ]
    
    print('Olá, o que você deseja fazer?')
    for i, opcao in enumerate(opcoes, 1):
       print(f'{i}) {opcao}')
    
    escolha = int(input('Digite o número da opção desejada: '))
    if escolha == 1:
        Livro.adicionar_catalogo(Livro)
    elif escolha == 2:
        Membro.cadastrar_membros(Livro)
    elif escolha == 3:
        Biblioteca.iniciar_pesquisa(Biblioteca)
    elif escolha == 4:
        Biblioteca.emprestar(Biblioteca)
    elif escolha == 5:
        Biblioteca.devolucao(Biblioteca)
    elif escolha == 6:
        print(Biblioteca.estante)
        main()
    elif escolha == 7:
        print(Biblioteca.nossos_membros)
    elif escolha == 8:
        Biblioteca.excluir_livro(Biblioteca)
    elif escolha == 9:
        Biblioteca.excluir_membro(Biblioteca)
    elif escolha == 10:
        pass
        
if __name__ == '__main__':
    main()