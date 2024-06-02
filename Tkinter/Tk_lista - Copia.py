from tkinter import *
from tkinter.ttk import *
import tkinter as tk
janela = Tk()

tree_view = Treeview(janela)
tree_view['columns'] = ('descrição', 'prioridade')

label_nome = Label(janela, text='Digite aqui o nome da nova tarefa')
entry_nome = Entry(janela, width=50)
label_nome.pack()
entry_nome.pack()

label_descricao = Label(janela, text='Digite aqui a descrição dessa tarefa')
entry_descricao = Entry(janela, width=50)
label_descricao.pack()
entry_descricao.pack()

label_prioridade = Label(janela, text='Digite aqui o nível de prioridade da tarefa (1 a 5)')
entry_prioridade = Entry(janela, width=50)
label_prioridade.pack()
entry_prioridade.pack()



def adicionar():
  nome = entry_nome.get()
  descricao = entry_descricao.get()
  prioridade = entry_prioridade.get()
  tree_view.insert("", END, text=nome, values=(descricao, prioridade, ))



def excluir():
  if tree_view.selection():
    item = tree_view.selection()[0]
    tree_view.delete(item)
    

add = Button(janela, text="Adicionar", command=adicionar )
add.pack()

tree_view.column('#0', width=100, minwidth=100, anchor='center')
# tree_view.column('tarefa', width=150, minwidth=150, anchor='center')
tree_view.column('descrição', width=150, minwidth=150, anchor='center')
tree_view.column('prioridade', width=150, minwidth=150, anchor='center')


tree_view.heading('#0', text='Tarefa')
# tree_view.heading('tarefa', text='Tarefa')
tree_view.heading('descrição', text='Descrição')
tree_view.heading('prioridade', text='Prioridade')

excluir_tarefa = Button(janela, text="Excluir tarefa", command=excluir)

tree_view.pack()
excluir_tarefa.pack()
janela.mainloop()