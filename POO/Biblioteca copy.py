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

    


    def ver_livros (self, estante):
        for livro in estante:
            # if livro['status'] == True:
                print("ID: {}, Título: {}, Autor: {}, Status: {}".format(livro['id'], livro['titulo'], livro['autor'], 'em estoque' if livro['status'] else 'emprestado'))



class Membro():
    def __init__(self, cadastro, nome, historico = None):
        self.cadastro = cadastro
        self.nome = nome
        self.historico = historico # provavelmente funcionará bem com dicionário

    def ver_membros (self):
        novo_membro = []
        for item in Biblioteca.nossos_membros:
            novo_membro.append(str(item))
            print(novo_membro[-1])
        return novo_membro


class Biblioteca():
    estante = []
    nossos_membros = []
    def init (self):
        self.catalogo_livros = []
        self.registro_membros = []
    
    # def bool_to_str(self, livro_escolhido):
    #     status_formatado = "em estoque" if livro_escolhido['status'] else "emprestado"
    #     return status_formatado


    # def __str__(self, livro_escolhido):
    #     status_formatado = "em estoque" if self.status else "emprestado"
    #     # return f"ID: {self.id}, Título: {self.titulo}, Autor: {self.autor}, Status: {status_formatado}"
    #     return status_formatado

    def adicionar_estante(self, item):
        self.estante.append(item)
        return self.estante

    def adicionar_catalogo(self): 
        print('Adicionando livro')
        for item in livros:
            titulo = item['titulo']
            id = item['id']
            autor = item['autor']
            status = item['status']
            livro = Livro(id, titulo, autor, status)
            Biblioteca.estante.append(livro.__dict__)
        livro.ver_livros(Biblioteca.estante)
        main()
        

    def alterar_status(self, livrin, novo_status):
        status_novin = ''
        for livro in self.estante:
            if livro['titulo'] == livrin:
                if livro['status'] != novo_status:
                    livro["status"] == novo_status
                    status_novin = 'emprestado'
                    
                elif livro["status"] == novo_status:
                    status_novin = 'emprestado'
            print(status_novin)
        return status_novin
                

                

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
            for livro in Biblioteca.estante:
                if livro['titulo'] == livro_escolhido:
                    if livro['status'] == False:
                        print(f'O livro {livro_escolhido} foi emprestado para outro cliente.')
                        self.pesquisar(Biblioteca)
                    else:
                        # resultado = self.bool_to_str(self, livro)
                        return f"O livro {livro['titulo']}, esscrito pelo autor {livro['autor']}, está {'em estoque' if True else 'emprestado'}"
                        
                    self.pesquisar(Biblioteca)
        
    
    def pesquisando_autor(self, autor_escolhido):
        for autor in Biblioteca.estante:
            if autor['autor'] == autor_escolhido:
                if autor['status'] == False:
                   print(f"O autor {autor_escolhido} escreveu o livro {autor['titulo']}, porém ele já foi emprestado para outro cliente.")
                else:
                    resultado2 = f"O autor {autor_escolhido} escreveu o livro {autor['titulo']}, e seu status é {'em estoque' if True else 'emprestado'}"
                    return resultado2
            elif autor_escolhido not in Biblioteca.estante:
                print(f"Não encontramos nenhum livro do autor {autor_escolhido}")
            
        
    def pesquisando_id(self, id_escolhido):   
        for id in Biblioteca.estante:
            if id['id'] == id_escolhido:
                if id['status'] == False:
                    print(f"O autor {id['autor']} escreveu o livro {id['titulo']}, porém ele já foi emprestado para outro cliente.")
                else:
                    resultado2 = f"O id {id_escolhido} refere-se ao livro {id['titulo']}, escrito por {id['autor']} e o status é {'em estoque' if True else 'Emprestado'}"
                    return resultado2
            # elif id['id'] != id_escolhido:
            #     print(f'Não encontramos nenhum livro com o id {id}')

    def pesquisando_membro(self, membro_escolhido):
        for membro in Biblioteca.nossos_membros:
            if membro['nome'] == membro_escolhido:
                print(f'Seu nome é {membro["nome"]} seu numero de cadastro é {membro["cadastro"]} e seu histórico é {membro["historico"]}')
                return membro_escolhido
            # elif membro['nome'] != membro_escolhido:
            #     print('Membro não encontrado')
   
        
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
            print(f"Resultados: {resultado_pesquisa}")
            
        elif escolha == 2:
            nome_autor = input('Digite aqui o nome do autor do livro: ')
            print(f'Vamos ver os livros de {nome_autor}...')
            self.pesquisando_autor(Biblioteca, nome_autor)
            resultado_pesquisa2 = self.pesquisando_autor(Biblioteca, nome_autor)
            print(f'Resultados:{resultado_pesquisa2}')

        elif escolha == 3:    
            id_livro = int(input("Digite aqui o id do liro: "))
            self.pesquisando_id(Biblioteca, id_livro)
            resultado_pesquisa3 = self.pesquisando_id(Biblioteca, id_livro)
            print(f'Resultados: {resultado_pesquisa3}')
  
        else:
            print('Opção inválida')
            self.pesquisar(Biblioteca)
        main()
        
    def emprestando(self, membro, livro_escolhido):
        final_result = self.alterar_status(Biblioteca, result, False)
        for pessoinha in membros:
            if pessoinha['nome'] == membro:
                history = {'Livro': livro_escolhido, 'Status': final_result}
                pessoinha['historico'].append(history)
            print(pessoinha)
           
            

    def emprestar(self):
      nome_membro = input('Digite aqui seu nome para localizarmos seu cadastro: ')
      result_nome = self.pesquisando_membro(Biblioteca, nome_membro)
      global result # Pra que esse global mesmo?
      result = self.pesquisar(Biblioteca)
     
      escolha = int(input(f'{result_nome}, gostaria de pegar o livro {result} emprestado? (1/2)'))
      if escolha == 1:
        self.emprestando(Biblioteca, result_nome, result)
        print(f'O livro {result}, foi emprestado.')
        main()
        
     
    

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

