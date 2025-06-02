import os
import shutil

def find_files_in_directory(base_directory, keyword):
    """Procura arquivos em um diretório e seus subdiretórios que contenham a palavra-chave no nome."""
    files_with_keyword = []
    for root, _, files in os.walk(base_directory):  # Ignora 'dirs' já que não será usado aqui
        for file in files:
            if keyword in file:  # Verifica se a palavra-chave está no nome do arquivo
                files_with_keyword.append(os.path.join(root, file))
    return files_with_keyword

def find_directory_by_keyword(base_directory, keyword):
    """Procura por um subdiretório que contenha a palavra-chave no nome dentro de um diretório base."""
    for root, dirs, _ in os.walk(base_directory):
        for dir_name in dirs:
            if keyword in dir_name:  # Verifica se a palavra-chave está no nome do diretório
                return os.path.join(root, dir_name)
    return None

def move_files_to_directory(files, target_directory):
    """Move uma lista de arquivos para o diretório de destino."""
    for file_path in files:
        target_path = os.path.join(target_directory, os.path.basename(file_path))
        try:
            shutil.move(file_path, target_path)
            print(f'Movido: {file_path} -> {target_path}')
        except Exception as e:
            print(f'Erro ao mover {file_path}: {e}')

# Caminhos de diretório
search_directory = os.path.expanduser("C:\\Users\\despachatur\\Documents")  # Caminho base para busca
target_directory = 'C:\\Users\\despachatur\\Documents'  # Diretório base onde o arquivo será movido
keyword = 'Comprovante'

# Passo 1: Procurar arquivos com a palavra-chave no diretório base
files_to_move = find_files_in_directory(search_directory, keyword)

# Passo 2: Procurar um diretório de destino com a palavra-chave dentro do diretório de destino especificado
target_subdirectory = find_directory_by_keyword(target_directory, keyword)

# Verifica se encontrou arquivos e um diretório de destino
if files_to_move and target_subdirectory:
    # Passo 3: Mover os arquivos para o diretório de destino
    move_files_to_directory(files_to_move, target_subdirectory)
else:
    print("Nenhum arquivo ou diretório correspondente foi encontrado.")
