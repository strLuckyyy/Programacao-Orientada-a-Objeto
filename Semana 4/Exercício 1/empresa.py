'''
Classe Empresa:
◦ Uma empresa tem um nome e dois funcionários do caixa.
◦ Crie um construtor que recebe todos os parâmetros para inicializar os atributos.
◦ Crie os métodos de acesso dos atributos desta classe (get e set).
◦ Crie um método imprime_info, que imprime as informações da classe.
'''
from funcionario import FuncionarioCaixa
from ficha import Ficha


class Empresa:
    def __init__(self, name: str, func_1: FuncionarioCaixa, func_2: FuncionarioCaixa) -> None:
        self.__name = name
        self.__func_1 = func_1
        self.__func_2 = func_2


    @property
    def name(self):
        return self.__name
    

    @name.setter
    def name(self, name):
        self.__name = name


    @property
    def func_1(self):
        return self.__func_1
    

    @func_1.setter
    def func_1(self, func):
        self.__func_1 = func
    

    @property
    def func_2(self):
        return self.__func_2
    

    @func_2.setter
    def func_2(self, func):
        self.__func_2 = func

    
    def imprimi_info(self):
        nome: list = ['Nome da Empresa']
        valor: list = [self.__name]

        info = Ficha('INFORMAÇÕES DA EMPRESA')
        info.titulo()
        info.conteudo(nome, valor)

        self.func_1.imprimi_info()
        self.func_2.imprimi_info()
