class Aluno():
    notas = {}

    def __init__(self, nome, idade, ano, matricula):
        self.nome = nome
        self.idade = idade
        self.ano = ano
        self.matricula = matricula

    def __str__(self) -> str:
        return f"Nome: {self.nome}, matricula: {self.matricula}"
    

class Professor():
    def __init__(self, nome, idade, salario, especialidade):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.especialidade = especialidade


class Controle_prof(Professor):
    def __init__(self, nome, idade, salario, especialidade, n_de_controle):
        super().__init__(nome, idade, salario, especialidade)
        self.n_de_controle = n_de_controle

    def lancar_notas(self):
        global notas
        controle = int(input('Digite aqui o seu número de cadastro: '))
        #aqui vai a matricula do aluno pro prof acessar
        matricula_aluno = input('Digite o número de matrícula do aluno: ') 
        nota = int(input('Digite aqui a nota do aluno: '))
        notas[self.especialidade] = nota, #aluno 
  
    def cadastro_professor(self):
        print('Novo professor:')
        nome = input('Digite aqui o nome do novo professor: ')
        idade = input('Digite aqui a idade do novo professor: ')
        salario = input('Digite aqui o salário bruto do novo professor: ')
        especialidade = input('Digite aqui a àrea de especialidade do novo professor: ')
        n_de_controle = int(input('Digite aqui o numero de cadastro desse professor: '))
        professor = Controle_prof(nome, idade, salario, especialidade, n_de_controle)
        self.professores.append(professor.__dict__)


class Escola():
    matriculados = []
    professores = []
    escolas = []

    def __init__(self, nome, endereco, segmento):
        self.nome = nome
        self.endereco = endereco
        self.segmento = segmento

    def matricular(self):
        print('Novo aluno:')
        nome = input('Digite aqui o nome do novo aluno: ')
        idade = input('Digite aqui a idade do aluno: ')
        ano = input('Digite aqui o ano em que o aluno será matriculado: ')
        matricula = input('Digite o numero da matricula do aluno: ')
        aluno = Aluno(nome, idade, ano, matricula)
        self.matriculados.append(aluno.__dict__)

    def cadastro_professor(self):
        print('Novo professor:')
        nome = input('Digite aqui o nome do novo professor: ')
        idade = input('Digite aqui a idade do novo professor: ')
        salario = input('Digite aqui o salário bruto do novo professor: ')
        especialidade = input('Digite aqui a àrea de especialidade do novo professor: ')
        professor = Professor(nome, idade, salario, especialidade)
        self.professores.append(professor.__dict__)

    def escola_info(self):
        
        nome = input('Digite o nome da escola: ')
        endereco = input('Digite aqui o endereço da escola: ')
        segmento = input('Digite aqui o segmento da escola: ')
        escola = Escola(nome, endereco, segmento)
        self.escolas.append(escola.__dict__)
        

def main():
    pt1 = int(input('Olá, Digite 1 para cadastros gerais e 2 para adicionar notas para alunos: '))
    if pt1 == 1:
        cadastros()
    else:
        Professor.lancar_notas()
    main()


def cadastros():
    inicio = int(input('Olá, digite 1 para cadastrar escola, 2 para professor, 3 para aluno ou 4 para verificar a lista de uma das opçôes abaixo: '))
    if inicio == 1:
        Escola.escola_info(Escola)
        print(Escola.escolas)
    elif inicio == 2:
        Escola.cadastro_professor(Escola)
        print(Escola.professores)
    elif inicio == 3:
        Escola.matricular(Escola)
        print(Escola.matriculados)

main()
