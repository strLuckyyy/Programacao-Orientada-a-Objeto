from funcionario import FuncionarioCaixa


class Empresa:
    def __init__(self, nome: str, funcionario1: FuncionarioCaixa, funcionario2: FuncionarioCaixa):
        self.__nome = nome
        self.__funcionario1 = funcionario1
        self.__funcionario2 = funcionario2

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def funcionario1(self):
        return self.__funcionario1

    @funcionario1.setter
    def funcionario1(self, funcionario1):
        self.__funcionario1 = funcionario1

    @property
    def funcionario2(self):
        return self.__funcionario2

    @funcionario2.setter
    def funcionario2(self, funcionario2):
        self.__funcionario2 = funcionario2

    def imprime_info(self):
        print("\nDADOS DA EMPRESA")
        print("\nDados do primeiro funcionário:")
        self.funcionario1.imprime_info()
        print("\nDados do segundo funcionário:")
        self.funcionario2.imprime_info()
