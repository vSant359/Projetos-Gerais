import unicodedata

# Função para remover acentos
def remover_acentos(texto):
    nfkd = unicodedata.normalize('NFKD', texto)
    return "".join([c for c in nfkd if not unicodedata.combining(c)])

# Função de pesquisa por nome
def pesquisar_livro_por_nome(termo_de_busca):
    termo_normalizado = remover_acentos(termo_de_busca).upper()  # Normaliza o termo de busca
    
    resultados = []
    for livro in livros:
        titulo_normalizado = remover_acentos(livro['titulo']).upper()  # Normaliza o título do livro
        
        if termo_normalizado in titulo_normalizado:
            resultados.append(livro)
    
    if resultados:
        for resultado in resultados:
            print(f"Título: {resultado['titulo']}, Autor: {resultado['autor']}, Status: {'Disponível' if resultado['status'] else 'Indisponível'}")
    else:
        print("Nenhum livro encontrado.")

# Lista de livros
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
pesquisar_livro_por_nome("Revolucao dos Bichos")
