#Nossa escola agora passará a lidar com uma lista de estudantes a serem cadastrados e uma lista de professores a serem cadastrados
# O método que cadastra professores e alunos ainda pertence à classe Escola e deve ser executado pelo objeto da classe escola na qual desejamos cadastrar aqueles estudantes.

#Será necessário criar classes que herdam das classes originárias, para que se adequém a esse novo contexto.

# Nesse novo caso a chave "ano" corresponde ao ano de ingresso do aluno na instituição
# A chave idade foi substituída pela chave data_nascimento
from Sistema_escolar_geral import Escola, Aluno, Professor

alunos = [
    {"nome": "Maria", "data_nascimento": "10/05/2005", "ano": 2023, "matricula": "A123"},
    {"nome": "João", "data_nascimento": "15/10/2002", "ano": 2024, "matricula": "B456"},
    {"nome": "Ana", "data_nascimento": "20/08/2003", "ano": 2022, "matricula": "C789"},
    {"nome": "Pedro", "data_nascimento": "25/03/2001", "ano": 2023, "matricula": "D321"},
    {"nome": "Julia", "data_nascimento": "05/12/2000", "ano": 2024, "matricula": "E654"},
    {"nome": "Lucas", "data_nascimento": "12/07/2002", "ano": 2022, "matricula": "F987"},
    {"nome": "Carla", "data_nascimento": "30/11/2003", "ano": 2023, "matricula": "G654"},
    {"nome": "Marcos", "data_nascimento": "18/09/2001", "ano": 2024, "matricula": "H321"},
    {"nome": "Lara", "data_nascimento": "28/02/2005", "ano": 2022, "matricula": "I987"},
    {"nome": "Gustavo", "data_nascimento": "08/06/2000", "ano": 2023, "matricula": "J654"}
]


professores = [
    {"nome": "Ana", "data_nascimento": "10/05/1980", "salario": 5000, "especialidade": "Ciências"},
    {"nome": "Carlos", "data_nascimento": "15/08/1975", "salario": 5500, "especialidade": "História"},
    {"nome": "Marta", "data_nascimento": "20/03/1985", "salario": 4800, "especialidade": "Português"},
    {"nome": "Pedro", "data_nascimento": "05/11/1970", "salario": 6000, "especialidade": "Matemática"}
]

class Aluno_novo(Aluno):
    def _init_(self, nome, data_nascimento, ano, matricula):
        super().__init__(self, nome, ano, matricula)
        self.data_nascimento = data_nascimento

    def __str__(self) -> str:
        return f"Nome: {self.nome}, matricula: {self.matricula}"


class Escola_nova(Escola):
    matriculados = []
    nossos_professores = []
    
    def _init_(self, nome, endereco, segmento):
        super().__init__(nome, endereco, segmento)
        
       


    def novo_aluno(self, lista_alunos):
        for aluno in lista_alunos:
            nome = aluno["nome"]
            data_nascimento = aluno["data_nascimento"]
            ano = aluno["ano"]
            matricula = aluno["matricula"]
            cadastro = Aluno_novo(nome,data_nascimento, ano, matricula)
            self.matriculados.append(cadastro)
            self.ver_matriculados()    
            
        

    def ver_matriculados(self):
        aluno_novo = []
        for item in reversed(self.matriculados):
            aluno_novo.append(str(item)) 
            print(aluno_novo)   
            return aluno_novo
        

    def novo_professor(self, lista_professores):
        for professor in lista_professores:
            nome = professor["nome"]
            data_nascimento = professor["data_nascimento"]
            salario = professor["salario"]
            especialidade = professor["especialidade"]
            cadastro = Novo_professor(nome, data_nascimento,  salario, especialidade)
            self.nossos_professores.append(cadastro)
            self.ver_professores()
    
  
            
            
        
   
    def ver_professores(self):
        professor_novo = []
        for item in reversed(self.nossos_professores):
            professor_novo.append(str(item)) 
            print(professor_novo)
            return professor_novo
        
        
escolas = Escola_nova('escola', 'rua1', 'nsei')

        
class Novo_professor(Professor):
    def __init__(self, nome, data_nascimento, salario, especialidade, idade=None):
        super().__init__(nome, salario, especialidade, idade)
        self.data_nascimento = data_nascimento

    def __str__(self) -> str:
        return f"Nome: {self.nome}, especialidade: {self.especialidade}"


escolas.novo_aluno(alunos)

escolas.novo_professor(professores)



#Nossa escola agora passará a lidar com uma lista de estudantes a serem cadastrados e uma lista de professores a serem cadastrados
# O método que cadastra professores e alunos ainda pertence à classe Escola e deve ser executado pelo objeto da classe escola na qual desejamos cadastrar aqueles estudantes.

#Será necessário criar classes que herdam das classes originárias, para que se adequém a esse novo contexto.

# Nesse novo caso a chave "ano" corresponde ao ano de ingresso do aluno na instituição
# A chave idade foi substituída pela chave data_nascimento
from Sistema_escolar_geral import Escola, Aluno, Professor

alunos = [
    {"nome": "Maria", "data_nascimento": "10/05/2005", "ano": 2023, "matricula": "A123"},
    {"nome": "João", "data_nascimento": "15/10/2002", "ano": 2024, "matricula": "B456"},
    {"nome": "Ana", "data_nascimento": "20/08/2003", "ano": 2022, "matricula": "C789"},
    {"nome": "Pedro", "data_nascimento": "25/03/2001", "ano": 2023, "matricula": "D321"},
    {"nome": "Julia", "data_nascimento": "05/12/2000", "ano": 2024, "matricula": "E654"},
    {"nome": "Lucas", "data_nascimento": "12/07/2002", "ano": 2022, "matricula": "F987"},
    {"nome": "Carla", "data_nascimento": "30/11/2003", "ano": 2023, "matricula": "G654"},
    {"nome": "Marcos", "data_nascimento": "18/09/2001", "ano": 2024, "matricula": "H321"},
    {"nome": "Lara", "data_nascimento": "28/02/2005", "ano": 2022, "matricula": "I987"},
    {"nome": "Gustavo", "data_nascimento": "08/06/2000", "ano": 2023, "matricula": "J654"}
]


professores = [
    {"nome": "Ana", "data_nascimento": "10/05/1980", "salario": 5000, "especialidade": "Ciências"},
    {"nome": "Carlos", "data_nascimento": "15/08/1975", "salario": 5500, "especialidade": "História"},
    {"nome": "Marta", "data_nascimento": "20/03/1985", "salario": 4800, "especialidade": "Português"},
    {"nome": "Pedro", "data_nascimento": "05/11/1970", "salario": 6000, "especialidade": "Matemática"}
]

class Aluno_novo(Aluno):
    def _init_(self, nome, data_nascimento, ano, matricula):
        super().__init__(self, nome, ano, matricula)
        self.data_nascimento = data_nascimento


class Escola_nova(Escola):
    def _init_(self, nome, endereco, segmento):
        super().__init__(nome, endereco, segmento)
        self.matriculados = []
        self.nossos_professores = []
       


    def novo_aluno(self, lista_alunos):
        for aluno in lista_alunos:
            nome = aluno["nome"]
            data_nascimento = aluno["data_nascimento"]
            ano = aluno["ano"]
            matricula = aluno["matricula"]
            cadastro = Aluno_novo(nome,data_nascimento, ano, matricula)
            self.matriculados.append(cadastro)
            
            
        return self.ver_matriculados

    def ver_matriculados(self):
        aluno_novo = []
        for item in self.matriculados:
            aluno_novo.append(str(item)) 
            return aluno_novo
        

    def novo_professor(self, lista_professores):
        for professor in lista_professores:
            nome = professor["nome"]
            data_nascimento = professor["data_nascimento"]
            salario = professor["salario"]
            especialidade = professor["especialidade"]
            cadastro = Novo_professor(nome,data_nascimento,salario, especialidade)
            self.nossos_professores.append(cadastro)
            
        return self.ver_professores
   
   
    def ver_professores(self):
        professor_novo = []
        for item in self.nossos_professores:
            professor_novo.append(str(item)) 
            return professor_novo
        
        
escolas = Escola_nova('escola', 'rua1', 'nsei')

        
class Novo_professor(Professor):
    def __init__(self, nome, data_nascimento, salario, especialidade) -> None:
        super().__init__(nome, salario, especialidade, idade=None)

        self.data_nascimento = data_nascimento



escolas.novo_aluno(alunos)

escolas.novo_professor(professores)


