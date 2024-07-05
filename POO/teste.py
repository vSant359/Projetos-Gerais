class Livro:
    def __init__(self, id, titulo, autor, status):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.status = status  # True para "em estoque", False para "emprestado"
    
    def __str__(self):
        status_formatado = "em estoque" if self.status else "emprestado"
        return f"ID: {self.id}, Título: {self.titulo}, Autor: {self.autor}, Status: {status_formatado}"


class Biblioteca:
    estante = []

class SistemaBiblioteca:
    def adicionar_catalogo(self):
        print('Adicionando livros ao catálogo...')
        for item in livros:
            livro_dict = {
                "id": item['id'],
                "titulo": item['titulo'],
                "autor": item['autor'],
                "status": item['status']  # Mantém o status como booleano
            }
            Biblioteca.estante.append(livro_dict)  # Adiciona o dicionário à estante
        self.ver_livros()

    def ver_livros(self):
        print('Catálogo de Livros:')
        for livro_dict in Biblioteca.estante:
            livro = Livro(livro_dict['id'], livro_dict['titulo'], livro_dict['autor'], livro_dict['status'])
            print(livro)  # Chama implicitamente livro.__str__()

# Lista de livros como dicionários
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

# Exemplo de uso
sistema = SistemaBiblioteca()
sistema.adicionar_catalogo()
