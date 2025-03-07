class Aluno:
    def __init__(self, nome, idade, matricula):
        self.__nome = nome
        self.__idade = idade
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    def __eq__(self, aluno):
        if id(self) == id(aluno):
            return True
        elif self.matricula == aluno.matricula:
            return True
        else:
            return False

    def imprime_info(self):
        print("\nDados do Aluno:")
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nMatrícula: {self.matricula}")