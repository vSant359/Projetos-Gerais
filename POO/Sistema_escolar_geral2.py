# Nossa escola agora passará a lidar com uma lista de estudantes a serem cadastrados e uma lista de professores a serem cadastrados
# O método que cadastra professores e alunos ainda pertence à classe Escola e deve ser executado pelo objeto da classe escola na qual desejamos cadastrar aqueles estudantes.

# Será necessário criar classes que herdam das classes originárias, para que se adequém a esse novo contexto.

# Nesse novo caso a chave "ano" corresponde ao ano de ingresso do aluno na instituição
# A chave idade foi substituída pela chave data_nascimento
from Sistema_escolar_geral import Escola, Aluno, Professor


alunos = [
    {"nome": "Maria", "data_nascimento": "10/05/2005",
        "ano": 2023, "matricula": "A123"},
    {"nome": "João", "data_nascimento": "15/10/2002",
        "ano": 2024, "matricula": "B456"},
    {"nome": "Ana", "data_nascimento": "20/08/2003",
        "ano": 2022, "matricula": "C789"},
    {"nome": "Pedro", "data_nascimento": "25/03/2001",
        "ano": 2023, "matricula": "D321"},
    {"nome": "Julia", "data_nascimento": "05/12/2000",
        "ano": 2024, "matricula": "E654"},
    {"nome": "Lucas", "data_nascimento": "12/07/2002",
        "ano": 2022, "matricula": "F987"},
    {"nome": "Carla", "data_nascimento": "30/11/2003",
        "ano": 2023, "matricula": "G654"},
    {"nome": "Marcos", "data_nascimento": "18/09/2001",
        "ano": 2024, "matricula": "H321"},
    {"nome": "Lara", "data_nascimento": "28/02/2005",
        "ano": 2022, "matricula": "I987"},
    {"nome": "Gustavo", "data_nascimento": "08/06/2000",
        "ano": 2023, "matricula": "J654"}
]


professores = [
    {"nome": "Ana", "data_nascimento": "10/05/1980",
        "salario": 5000, "especialidade": "Ciências"},
    {"nome": "Carlos", "data_nascimento": "15/08/1975",
        "salario": 5500, "especialidade": "História"},
    {"nome": "Marta", "data_nascimento": "20/03/1985",
        "salario": 4800, "especialidade": "Português"},
    {"nome": "Pedro", "data_nascimento": "05/11/1970",
        "salario": 6000, "especialidade": "Matemática"}
]


class Aluno_novo(Aluno):
    def _init_(self, nome, data_nascimento, ano, matricula):
        super().__init__(self, nome, ano, matricula)
        self.data_nascimento = data_nascimento
        self.notas = {}

    def __str__(self) -> str:
        return f"Nome: {self.nome}, matricula: {self.matricula}"


class Escola_nova(Escola):

    matriculados = []
    nossos_professores = []
    escola = []

    def _init_(self, nome, endereco, segmento):
        super().__init__(nome, endereco, segmento)

    def __str__(self) -> str:
        return f"Nome: {self.nome}, segmento: {self.segmento}"

    def cadastro_escola(self):
        nome = input('Digite o nome da escola: ')
        endereco = input('Digite o endereço da escola: ')
        segmento = input('Digite o segmento da escola: ')
        cadastro = Escola_nova(nome, endereco, segmento)
        self.escola.append(cadastro)
        self.ver_escolas(Escola_nova)

    def ver_escolas(self):
        escola_nova = []
        for item in (self.escola):
            escola_nova.append(str(item))
            print(escola_nova)
            return escola_nova

    def novo_aluno(self, lista_alunos):
        for aluno in lista_alunos:
            nome = aluno["nome"]
            data_nascimento = aluno["data_nascimento"]
            ano = aluno["ano"]
            matricula = aluno["matricula"]
            cadastro = Aluno_novo(nome, data_nascimento, ano, matricula)
            self.matriculados.append(cadastro)
            self.ver_matriculados(Escola_nova)

    def ver_matriculados(self):
        for coiso in self.matriculados:
            aluno_novo = []
            for item in reversed(self.matriculados):
                aluno_novo.append(str(item))
                print(aluno_novo)
                return aluno_novo


    def novo_aluno_manual(self):
        self.ver_matriculados(Escola_nova)
        print('Novo aluno:')
        nome = input('Digite aqui o nome do novo aluno: ')
        data_nascimento = input('Digite aqui a data de nascimento do aluno: ')
        ano = input('Digite aqui o ano em que o aluno será matriculado: ')
        matricula = input('Digite o numero da matricula do aluno: ')
        aluno = Aluno_novo(nome, data_nascimento, ano, matricula)
        Escola_nova.novo_aluno(Escola_nova, alunos)
        self.matriculados.append(aluno)
        self.ver_matriculados(Escola_nova)


    def novo_professor(self, lista_professores):
        for professor in lista_professores:
            nome = professor["nome"]
            data_nascimento = professor["data_nascimento"]
            salario = professor["salario"]
            especialidade = professor["especialidade"]
            cadastro = Novo_professor(
                nome, data_nascimento,  salario, especialidade)
            self.nossos_professores.append(cadastro)
            self.ver_professores(Escola_nova)

    def ver_professores(self,):
        professor_novo = []
        for item in reversed(self.nossos_professores):
            professor_novo.append(str(item))
            print(professor_novo)
            return professor_novo


class Novo_professor(Professor):
    notas = []

    def __init__(self, nome, data_nascimento, salario, especialidade, idade=None):
        super().__init__(nome, salario, especialidade, idade)
        self.data_nascimento = data_nascimento

    def __str__(self) -> str:
        return f"Nome: {self.nome}, especialidade: {self.especialidade}"

    def lancar_notas(self):

        nova_nota = {
            'Aluno': ' ',
            'Professor': '',
            'Matéria': ' ',
            'Nota': ' '
        }
        materia = input('Digite aqui a sua matéria: ')
        for prof in professores:
            if prof['especialidade'] == materia:
                nova_nota['Professor'] = prof['nome']
            # else:
            #     print('Não há nenhum professor cadastrado com essa matéria.')
            #     self.lancar_notas(Novo_professor)

        matricula_aluno = input('Digite o número de matrícula do aluno: ')
        nota = int(input('Digite aqui a nota do aluno: '))

        for crianca in alunos:
            if crianca['matricula'] == matricula_aluno:
                nova_nota['Aluno'] = crianca['nome']
        nova_nota['Matéria'] = materia
        nova_nota['Nota'] = nota
        Novo_professor.notas.append(nova_nota)
        print(self.notas)

    def set_nota():
        pass


 

def menu():
    opcao = True
    while True:
        print('Olá o que você deseja fazer?')
        print('1 - Cadastrar uma nova escola')
        print('2 - Cadastrar um novo professor')
        print('3 - Cadastrar um novo aluno')
        print('4 - Lançar nota para um aluno')
        print('5 - Vizualizar as informações de toda a escola')
        opcao = False
        escolha = int(input('Digite aqui o número da opção desejada: '))
        if escolha == 1:
            Escola_nova.cadastro_escola(Escola_nova)
        elif escolha == 2:
            Escola_nova.novo_professor(Escola_nova, professores)
        elif escolha == 3:
            
            Escola_nova.novo_aluno_manual(Escola_nova)
        elif escolha == 4:
            Novo_professor.lancar_notas(Novo_professor)
        else:
            Escola_nova.ver_escolas(Escola_nova)
            Escola_nova.ver_professores(Escola_nova)
            Escola_nova.ver_matriculados(Escola_nova)


menu()


# escolas.novo_professor(professores)