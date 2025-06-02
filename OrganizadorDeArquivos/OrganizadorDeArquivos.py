import os
import shutil
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import magic

# Criando a janela principal
root = tk.Tk()
root.title("Organizador de Arquivos")
root.geometry("500x300")  # Define um tamanho fixo para a janela
root.resizable(False, False)  # Impede redimensionamento

# Estilizando a interface
style = ttk.Style()
style.configure("TButton", font=("Arial", 10), padding=5)
style.configure("TLabel", font=("Arial", 10))
style.configure("TEntry", font=("Arial", 10))

# Funções para seleção de diretórios
def selecionar_origem():
    pasta = filedialog.askdirectory()
    origem_var.set(pasta)

def selecionar_destino():
    pasta = filedialog.askdirectory()
    destino_var.set(pasta)

# Função para mover os arquivos
def move_items():
    origem = origem_var.get()
    destino = destino_var.get()
    tipos = tipos_var.get().split()


    if not origem or not destino or not tipos:
        messagebox.showerror("Erro", "Preencha todos os campos antes de organizar os arquivos.")
        return

    if not os.path.exists(destino):
        os.makedirs(destino)
    
    files = os.listdir(origem)
    movidos = 0

    items = []
    for nome in os.listdir(origem):
        full_path = os.path.join(origem, nome)

        # Verifica se é um arquivo regular e se tem permissão de leitura
        if not os.path.isfile(full_path):
            print(f"[IGNORADO] Não é um arquivo: {nome}")
            continue
        if not os.access(full_path, os.R_OK):
            print(f"[SEM ACESSO] Permissão negada para: {nome}")
            continue

        try:
            file_type = magic.Magic(mime=True).from_file(os.fsdecode(full_path))
            print(f"[TIPO] {nome}: {file_type}")

            for tipo in tipos:
                if tipo.lower() in file_type.lower():
                    items.append(nome)
                    break

            if file_type == 'application/pdf':
                items.append(nome)
                print(items)
        except PermissionError:
            print(f"[ERRO] Permissão negada ao analisar: {nome}")
        except Exception as e:
            print(f"[ERRO] Falha ao identificar tipo de arquivo '{nome}': {e}")

    for nome in items:
        origem_completa = os.path.join(origem, nome)
        destino_completo = os.path.join(destino, nome)

        try:
            shutil.move(origem_completa, destino_completo)
            movidos += 1
            print(f"[MOVIDO] {nome} -> {destino_completo}")
        except Exception as e:
            print(f"[ERRO AO MOVER] {nome}: {e}")

    print(f"\n✅ Total de arquivos PDF movidos: {movidos}")
    messagebox.showinfo("Concluído", f"{movidos} arquivos movidos com sucesso!")

# Criando variáveis para armazenar diretórios
origem_var = tk.StringVar()
destino_var = tk.StringVar()
tipos_var = tk.StringVar()

# Criando um frame centralizado para organizar os widgets
frame = ttk.Frame(root, padding=10)
frame.pack(expand=True)

# Labels e Entradas
ttk.Label(frame, text="Diretório de Origem:").grid(row=0, column=0, sticky="w", pady=2)
ttk.Entry(frame, textvariable=origem_var, width=40).grid(row=0, column=1, padx=5, pady=2)
ttk.Button(frame, text="Selecionar", command=selecionar_origem).grid(row=0, column=2, pady=2)

ttk.Label(frame, text="Diretório de Destino:").grid(row=1, column=0, sticky="w", pady=2)
ttk.Entry(frame, textvariable=destino_var, width=40).grid(row=1, column=1, padx=5, pady=2)
ttk.Button(frame, text="Selecionar", command=selecionar_destino).grid(row=1, column=2, pady=2)

ttk.Label(frame, text="Tipos de Arquivos (separados por espaço):").grid(row=2, column=0, columnspan=2, sticky="w", pady=5)
ttk.Entry(frame, textvariable=tipos_var, width=50).grid(row=3, column=0, columnspan=3, pady=5)

# Botão para iniciar a organização
ttk.Button(frame, text="Organizar Arquivos", command=move_items).grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
