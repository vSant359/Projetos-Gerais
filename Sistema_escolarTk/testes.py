import tkinter as tk
from tkinter import StringVar, OptionMenu

# Função a ser chamada quando uma opção for selecionada
def option_selected(value):
    print(f'Opção selecionada: {value}')

# Criação da janela principal
root = tk.Tk()
root.title('Exemplo de Dropdown')

# Variável que armazenará a opção selecionada
selected_option = StringVar(root)
selected_option.set('Opção 1')  # Definir valor padrão

# Lista de opções do dropdown
options = ['Opção 1', 'Opção 2', 'Opção 3', 'Opção 4']

# Criação do dropdown (OptionMenu)
dropdown = OptionMenu(root, selected_option, *options, command=option_selected)
dropdown.pack(pady=20)

# Loop principal da interface gráfica
root.mainloop()
