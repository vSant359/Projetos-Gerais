from tkinter import *
from tkinter.ttk import *

ten_emails = ['amanda@gmail.com', 'thiago@gmail.com', 'luis@gmail.com', 'victor@gmail.com', 'carla@gmail.com', 'raiane@gmail.com', 'camille@gmail.com', 'roberto@gmail.com', 'jose@gmail.com', 'felipe@gmail.com']

ten_names = ['Amanda', 'Thiago', 'Luis', 'Victor', 'Carla', 'Raiane', 'Camille', 'Roberto', 'José', 'Felipe']

# Criar um Tree View utilizando o TK inter, com duas colunas contendo as informações de nome e email cadastrados.

janela = Tk()

tree_view = Treeview(janela)
tree_view['columns'] = ('nome', 'email')

label_nome = Label(janela, text='Digite aqui seu nome')
entry_nome = Entry(janela, width=50)
label_nome.pack()
entry_nome.pack()

label_email = Label(janela, text="Digite aqui seu e-mail")
entry_email = Entry(janela, width=50)
label_email.pack()
entry_email.pack()

def add():
  nome = entry_nome.get()
  email = entry_email.get()
  tree_view.insert("", END, text=i, values=(nome, email))
  

botao = Button(janela, text="Adicionar", command=add)
botao.pack()

tree_view.column('#0', width=100, minwidth=100, anchor='center')
tree_view.column('nome', width=150, minwidth=150, anchor='center')
tree_view.column('email', width=150, minwidth=150, anchor='center')

tree_view.heading('#0', text='ID')
tree_view.heading('nome', text='NOME')
tree_view.heading('email', text='EMAIL')

i = 1
for x,y in zip(ten_names, ten_emails):
    
    tree_view.insert("", END, text=i, values=(x, y))
    i = i+1
tree_view.pack()
janela.mainloop()
