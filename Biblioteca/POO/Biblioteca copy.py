import unidecode

livros = [
    {"id": 0, "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "status": True},
    {"id": 1, "titulo": "1984", "autor": "George Orwell", "status": False},
    {"id": 2, "titulo": "Dom Quixote", "autor": "Miguel de Cervantes", "status": True},
    {"id": 3, "titulo": "Moby Dick", "autor": "Herman Melville", "status": False},
    {"id": 4, "titulo": "A Revolução dos Bichos", "autor": "George Orwell", "status": True},
    {"id": 5, "titulo": "Guerra e Paz", "autor": "Liev Tolstói", "status": False},
    {"id": 6, "titulo": "Orgulho e Preconceito", "autor": "Jane Austen", "status": True},
    {"id": 7, "titulo": "Ulisses", "autor": "James Joyce", "status": False},
    {"id": 8, "titulo": "A Metamorfose", "autor": "Franz Kafka", "status": True},
    {"id": 9, "titulo": "O Grande Gatsby", "autor": "F. Scott Fitzgerald", "status": False}
]




membros = [
    {"cadastro": 1, "nome": "Ana Silva", "historico": []},
    {"cadastro": 2, "nome": "Bruno Costa", "historico": []},
    {"cadastro": 3, "nome": "Carla Souza", "historico": []},
    {"cadastro": 4, "nome": "Daniel Oliveira", "historico": []},
    {"cadastro": 5, "nome": "Elena Ferreira", "historico": []},
    {"cadastro": 6, "nome": "Felipe Santos", "historico": []},
    {"cadastro": 7, "nome": "Gabriela Pereira", "historico": []},
    {"cadastro": 8, "nome": "Henrique Lima", "historico": []},
    {"cadastro": 9, "nome": "Isabel Mendes", "historico": []},
    {"cadastro": 10, "nome": "João Almeida", "historico": []}
     ]



class Livro():
    def __init__(self, id, titulo, autor, status):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.status = status

    def __repr__ (self, estante): #Com essa def eu controlo como que os livros serão apresentados ao user e garanto que ele não retornará o valor Bool para o user.
        for livro in estante:
            print("ID: {}, Título: {}, Autor: {}, Status: {}".format(livro['id'], livro['titulo'], livro['autor'], 'em estoque' if livro['status'] else 'emprestado'))
        main()
    
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
    def __init__(self, cadastro, nome, historico = None):
        self.cadastro = cadastro
        self.nome = nome
        self.historico = historico # provavelmente funcionará bem com dicionário

    def ver_membros (self):
        novo_membro = []
        for item in Biblioteca.nossos_membros:
            novo_membro.append(str(item))
            print(novo_membro[-1]) #print -1 garantirá que sempre seja impresso o último valor cadastrado.
        return novo_membro


class Biblioteca():
    estante = []
    nossos_membros = []
    def init (self):
        self.catalogo_livros = []
        self.registro_membros = []
    
   
    def adicionar_estante(self, item):
        self.estante.append(item)
        return self.estante
    

    def alterar_status(self, livrin): #tenho que ver esse trem porque não ta funcionando
        for livro in self.estante:
            if livro['titulo'] == livrin:
                if livro['status']:
                    livro.status = False
                return livro
                

    def cadastrar_membros(self):
        for item in membros:
            cadastro = item['cadastro']
            nome = item['nome']
            historico = item['historico']
            membro = Membro (cadastro, nome, historico)
            Biblioteca.nossos_membros.append(membro.__dict__)
        Membro.ver_membros(Membro)
        main()
      

    def pesquisando_nome(self, livro_escolhido):
            livro_escolhido_normalizado = unidecode.unidecode(livro_escolhido.lower())

            for livro in Biblioteca.estante:
                titulo_normalizado = unidecode.unidecode(livro["titulo"].lower())
                if titulo_normalizado == livro_escolhido_normalizado:
                    if livro['status'] == False:
                        print(f'O livro {livro["titulo"]} foi emprestado para outro cliente.')
                        self.pesquisar(Biblioteca)
                        return None # Retorna None para indicar que o livro foi encontrado, mas já está emprestado
                    else:
                        return livro
            # Se o loop terminar e não encontrar o livro, exibe a mensagem
            return None
    
    # def pesquisando_nome_devolucao(self, livro_escolhido):
    #     for livro in Biblioteca.estante:
    #         if livro['titulo'] == livro_escolhido:
    #             return livro
    #     print(f"Não encontramos nenhum livro com o nome {livro_escolhido}")
    #     return None

        
    
    def pesquisando_autor(self, autor_escolhido):
        autor_escolhido_normalizado = unidecode.unidecode(autor_escolhido.lower())

        for autor in Biblioteca.estante:
            autor_normalizado = unidecode.unidecode(autor["autor"])
            if autor_normalizado == autor_escolhido_normalizado:
                if autor['status'] == False:
                   print(f"O autor {autor_escolhido} escreveu o livro {autor['titulo']}, porém ele já foi emprestado para outro cliente.")
                   self.pesquisar(Biblioteca)
                   return None
                else:
                    return autor
        return None
            
        
    def pesquisando_id(self, id_escolhido):
        for livro in Biblioteca.estante:
            if livro['id'] == id_escolhido:
                if livro['status'] == False:
                    print(f"O autor {livro['autor']} escreveu o livro {livro['titulo']}, porém ele já foi emprestado para outro cliente.")
                    self.pesquisar(Biblioteca)
                    return None  # Retorna None para indicar que o livro foi encontrado, mas já está emprestado
                else:
                    return livro
        # Se o loop terminar e não encontrar o livro, exibe a mensagem
        return None


    def pesquisando_membro(self, membro_escolhido):
        for membro in Biblioteca.nossos_membros:
            if membro['nome'] == membro_escolhido:
                print(f'Seu nome é {membro["nome"]} seu numero de cadastro é {membro["cadastro"]} e seu histórico é {membro["historico"]}')
                return membro
        # Se o loop terminar e não encontrar o livro, exibe a mensagem  
        print('Membro não encontrado')
        return None
   
        
    def pesquisar(self):
        print('Como você gostaria de pesquisar seu livro?')
        print('1) Pelo nome do livro')
        print('2) Pelo nome do autor')
        print('3) Pelo id do livro')
        escolha = int(input('Digite o numero da opção desejada: '))
        if escolha == 1:
            global titulo
            livro_escolhido = input('Digite o título do livro que está procurando: ')
            self.pesquisando_nome(Biblioteca, livro_escolhido)
            resultado_pesquisa = self.pesquisando_nome(Biblioteca, livro_escolhido)
            if resultado_pesquisa is not None:
                print(f"O livro {resultado_pesquisa['titulo']}, esscrito pelo autor {resultado_pesquisa['autor']}, está {'em estoque' if True else 'emprestado'}")
                return resultado_pesquisa
            else:
                print(f"Não localizamos o livro {livro_escolhido}")
        
        elif escolha == 2:
            nome_autor = input('Digite aqui o nome do autor do livro: ')
            print(f'Vamos ver os livros de {nome_autor}...')
            self.pesquisando_autor(Biblioteca, nome_autor)
            resultado_pesquisa2 = self.pesquisando_autor(Biblioteca, nome_autor)
            if resultado_pesquisa2 is None:
                print(f"Não encontramos nenhum livro do autor {nome_autor}")
                return resultado_pesquisa2
            else:
                print(f"O autor {resultado_pesquisa2['autor']} escreveu o livro {resultado_pesquisa2['titulo']}, e seu status é {'em estoque' if True else 'emprestado'}")
                

        elif escolha == 3:
            id_livro = None   
            try:
                id_livro = int(input("Digite aqui o id do livro: "))
                resultado_pesquisa3 = self.pesquisando_id(Biblioteca, id_livro)
                if resultado_pesquisa3 is not None:
                    print(f"O id {resultado_pesquisa3['id']} refere-se ao livro {resultado_pesquisa3['titulo']}, escrito por {resultado_pesquisa3['autor']} e o status é {'em estoque' if True else 'Emprestado'}")
                    return resultado_pesquisa3
                else:
                    print(f"Não encontramos nenhum livro com o ID {id_livro}")
                    self.pesquisar(Biblioteca)
            except ValueError:
                print(f"O id do livro deve ser um número inteiro.")
                self.pesquisar(Biblioteca)
            
        else:
            print('Opção inválida')
            self.pesquisar(Biblioteca)
        main()
        
        
    def emprestando(self, membro, livro_escolhido):
        final_result = self.alterar_status(Biblioteca, livro_escolhido)
        membro['historico'].append(final_result)
        print(membro)


    def emprestar(self):
      nome_membro = input('Digite aqui seu nome para localizarmos seu cadastro: ')
      result_nome = self.pesquisando_membro(Biblioteca, nome_membro)
      if result_nome == None:
          print(f'Não conseguimos localizar o membro {nome_membro}')
          self.emprestar(self)
      else:
        result = self.pesquisar(Biblioteca)
        escolha = int(input(f"{result_nome['nome']}, gostaria de pegar o livro {result['titulo']} emprestado? (1/2)"))
        if escolha == 1:
            final_result = self.alterar_status(Biblioteca, result)
            result_nome['historico'].append(final_result)
            print(f"O livro {result['titulo']}, foi emprestado.")
            main()


    def devolucao(self):
        print('Para devolver o seu livro, primeiro vamos localizar seu cadastro')
        teu_nome = input('Digite aqui seu nome: ')
        membro_da_vez = self.pesquisando_membro(self, teu_nome)
        print('Agora vamos localizar qual livro você deseja devolver')
        nome_livro = input('Digite aqui o nome do livro que irá devolver: ')
        livro_da_vez = self.pesquisando_nome(self, nome_livro)
        escolha = input(f"Você gostaria de devolver o livro {livro_da_vez}?(s/n) ")
        if escolha == "s":
            atualizacao = self.alterar_status(Biblioteca)
            print(f"Certo, o livro {atualizacao['titulo']} foi devolvido a biblioteca, agora ele está {'em estoque' if True else 'emprestado'}")


        
def main():
    print('Olá, o que você deseja fazer?')
    print('1) Adicionar um livro ao catálogo')
    print('2) Cadastrar um novo membro')
    print('3) Pesquisar um livro dentro do catálogo')
    print('4) Emprestar um livro a um membro')
    print('5) Registrar a devolução do livro para a biblioteca')
    print('6) Ver todos os livros na biblioteca')
    escolha = int(input('Digite o número da opção desejada: '))
    if escolha == 1:
        Livro.adicionar_catalogo (Biblioteca)
    elif escolha == 2:
        Biblioteca.cadastrar_membros (Biblioteca)
    elif escolha == 3:
        Biblioteca.pesquisar (Biblioteca)
    elif escolha == 4:
        Biblioteca.emprestar(Biblioteca)
    elif escolha == 5:
        Biblioteca.devolucao(Biblioteca)
    elif escolha == 6:
        Livro.ver_livros(Livro, livros)
if __name__ == '__main__':
    main()

