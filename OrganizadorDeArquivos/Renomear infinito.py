import os

def rename_files_in_directory(directory):
    # Inicia o contador
    counter = 421
    renamed_files = set()  # Para armazenar os arquivos já renomeados

    # Lista os arquivos da pasta e filtra apenas os arquivos (não diretórios)
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    if files:
        # Ordena os arquivos numericamente (extrai os números do nome dos arquivos)
        files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))  # Ordenação numérica com base no número do nome do arquivo

        # Itera sobre os arquivos na ordem ordenada
        for last_file in files:
            if last_file not in renamed_files:
                file_extension = os.path.splitext(last_file)[-1]  # Mantém a extensão do arquivo
                new_name = f"2018.{counter}{file_extension}"
                old_path = os.path.join(directory, last_file)
                new_path = os.path.join(directory, new_name)

                # Verifica se o novo nome já existe
                if  not os.path.exists(new_path):
                    os.rename(old_path, new_path)
                    renamed_files.add(last_file)  # Marca o arquivo como renomeado
                    print(f"Renomeado: {last_file} -> {new_name}")
                    counter += 1  # Incrementa o contador

    print("\nTodos os arquivos foram renomeados.")

# Defina o diretório onde estão os arquivos que você quer renomear
directory_path = "C:\\Users\\despachatur\\Documents\\teste2"

rename_files_in_directory(directory_path)
