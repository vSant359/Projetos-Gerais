from tkinter import * # type: ignore
from tkinter.ttk import * # type: ignore
import json

janela = Tk()

tarefas = [{
  
}]



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
  
  # tree_view.insert("", END, iid=len(tarefas)-1, text=nome, values=(descricao, prioridade))
  
  tarefa = {
        'Nome': '',
        'Descrição': '',
        'Prioridade': ''
    }
  tarefa['Nome'] = nome
  tarefa['Descrição'] = descricao
  tarefa['Prioridade'] = prioridade
  tarefas.append(tarefa)
  print(tarefas)



  


def excluir():
  if tree_view.selection():
    item = tree_view.selection()[0]
    tree_view.delete(item)
    # del tarefas[int(item)]


add = Button(janela, text="Adicionar", command=adicionar )
add.pack()
tree_view.column('#0', width=250, minwidth=250,  anchor='center')
tree_view.column('descrição', width=300, minwidth=300, anchor='center')
tree_view.column('prioridade', width=300, minwidth=300, anchor='center')

tree_view.config(height=30)

tree_view.heading('#0', text='Tarefa')
tree_view.heading('descrição', text='Descrição')
tree_view.heading('prioridade', text='Prioridade')

def certeza():
  
  ctz = Tk()
  
  confirmacao = Label(ctz, text="Você tem certeza que quer apagar essa tarefa? Esssa ação não pode ser desfeita.")
  sim = Button(ctz, text="Sim", command=lambda: [excluir(), ctz.destroy()], )
  nao = Button(ctz, text="Não", command=ctz.destroy)
  confirmacao.pack()
  sim.pack()
  nao.pack()
  
  ctz.mainloop()
  

excluir_tarefa = Button(janela, text="Excluir tarefa", command=certeza)

def salvar():

  with open('dados.json', 'w', encoding='utf-8') as file:
    json.dump(tarefas, file, ensure_ascii=False, indent=4)
    janela.destroy()

janela.protocol("WM_DELETE_WINDOW", salvar)


tree_view.pack()
excluir_tarefa.pack()
janela.mainloop()


    

    
