from tkinter import * 
from tkinter.ttk import * 

janela = Tk()
janela.title('Sistema Escolar Geral')

def opcao_selecionada(value):
    if opcao_atual == 'Cadastrar Alunos':
        Alunos.cadastrar_alunos()

label_selecao = Label(janela, text='Olá, escolha abaixo a opção que deseja.')
label_selecao.pack()
opcao_atual = StringVar(janela)
opcao_atual.set('Selecionar...')

opcoes = ['Cadastrar Alunos', 'Cadastrar Escola', 'Cadastrar Professores', 'Lançar Notas']


dropdown = OptionMenu(janela, opcao_atual, *opcoes, command=opcao_selecionada)
dropdown.pack(pady=20)

selecionar = Button(janela, text='Vamos lá', command=opcao_selecionada)
selecionar.pack()
class Alunos():


    def cadastrar_alunos():
        janela_alunos = Tk()
        janela_alunos.title('Cadastro de Alunos')

        treeview = Treeview(janela_alunos)
        treeview['columns'] = ('nome', 'idade', 'ano', 'matricula')

        label_nome = Label(janela_alunos, text='Digite aqui o nome do novo aluno:')
        entry_nome = Entry(janela)
        label_nome.pack()
        entry_nome.pack()

        label_idade = Label(janela_alunos, text='Digite a idade do aluno')
        entry_idade = Entry(janela_alunos)
        label_idade.pack()
        entry_idade.pack()



janela.mainloop()