'''
Classe FuncionarioCaixa:
◦ Possui um nome, um endereço e uma calculadora.
◦ Crie um construtor que recebe os parâmetros para inicializar todos os atributos.
◦ Crie os métodos de acesso dos atributos desta classe (get e set).
◦ Crie os métodos soma, subtrai, multiplica, divide,
eleva_ao_quadrado e eleva_ao_cubo. Cada método destes deve chamar o
método correspondente da calculadora, retornando o valor obtido na operação.
◦ Crie um método chamado imprime_info, que não recebe parâmetros de
entrada e imprime na tela as informações da classe, inclusive da calculadora
(sem as operações, apenas os atributos).
'''
from calculadora import Calculadora
from ficha import Ficha



class FuncionarioCaixa:
    def __init__(self, name: str, adress: str, calculator: Calculadora) -> None:
        self.__name = name
        self.__adress = adress
        self.__calculator = calculator

    
    @property
    def name(self):
        return self.__name
    

    @name.setter
    def name(self, name):
        self.__name = name
    

    @property
    def adress(self):
        return self.__adress
    

    @adress.setter
    def adress(self, adress):
        self.__adress = adress


    @property
    def calculator(self):
        return self.__calculator
    

    @calculator.setter
    def calculator(self, calc):
        self.__calculator = calc


    def nameUpper(self) -> str:
        return self.__name.upper()


    def soma(self, value_1: float, value_2: float) -> float:
        return self.calculator.soma(value_1, value_2)
    

    def subtracao(self, value_1: float, value_2: float) -> float:
        return self.calculator.subtracao(value_1, value_2)
    

    def multip(self, value_1: float, value_2: float) -> float:
        return self.calculator.multip(value_1, value_2)
    

    def divisao(self, value_1: float, value_2: float) -> float:
        return self.calculator.divisao(value_1, value_2)
    

    def exponenciacao(self, value_1: int, expoente: int = 2) -> int:
        return self.exponenciacao(value_1, expoente)


    def imprimi_info(self):
        nome: list = ['Nome', 'Endereço']
        valor: list = [self.__name, self.__adress]

        info = Ficha('INFORMAÇÕES DO FUNCIONÁRIO')
        info.titulo()
        info.conteudo(nome, valor)

        self.calculator.imprime_info()
