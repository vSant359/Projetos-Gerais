def normalizar_texto(self, texto):
        return unidecode.unidecode(texto.lower)
    
    
    def pesquisar(self, tipo, valor):
        valor_normalizado = self.normalizar_texto(str(valor))

        campo = 'titulo' if tipo == 1 else 'autor' if tipo == 2 else 'id'

        for livro in self.estante:
            campo_valor_normalizado = self.normalizar_texto(str(livro[campo]))
            if campo_valor_normalizado == valor_normalizado:
                if  not livro['status']:
                    print(f"O livro {livro['titulo']} já foi emprestado.")
                    return None
                return livro
        print(f"Não encontramos nenhum livro com {campo} {valor}.")
        return None
    
    def pesquisar_membro(self, nome_membro):
        for membro in self.nossos_membros:
            if membro['nome'] == nome_membro:
                print(f"Nome: {membro['nome']}, Cadastro: {membro['cadastro']}, Histórico: {membro['historico']}")
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
            resultado = self.pesquisar(tipo, valor)

            if resultado:
                print(f"O livro {resultado['titulo']} de {resultado['autor']} está {'em estoque' if resultado['status'] else 'emprestado'}.")

        except ValueError as e:
            print(e)
            self.iniciar_pesquisa()