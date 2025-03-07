#   Trabalho do Grau B de Programação Orientada a Objetos de Abrahão Francis e Lucas Moraes.

from process import Process
from utility import Utility

k = Utility()

class ComputingProcess(Process):

#   inicialia o processo de computação recebendo um 'pid' da fila de processos, os número da operação e o operador
#   e também define seu tipo como 'Computing Process' na sua superclasse.
    def __init__(self, primeiroNumero : float, operador : str, segundoNumero : float, pid : int) -> None: 
        super().__init__('Computing Process', pid)
        self.__primeiroNum = primeiroNumero
        self.__operador = operador
        self.__segundoNum = segundoNumero

    @property
    def primeiroNumero(self) -> float:
        return self.__primeiroNum
    
    @property
    def operador(self) -> str:
        return self.__operador
    
    @property
    def segundoNumero(self) -> float:
        return self.__segundoNum
    
    @primeiroNumero.setter
    def primeiroNumero(self, newNum) -> None:
        self.__primeiroNum = newNum

    @segundoNumero.setter
    def segundoNumero(self, newNum) -> None:
        self.__segundoNum = newNum

    @operador.setter
    def operador(self, newOperador) -> None:
        self.__operador = newOperador

#   imprime o tipo de processo sendo executado, a expressão matemática e o resultado dela. isso se aplica para todas as quatro abaixo.
    def __soma(self) -> float:
        k.separacao()
        print(f'{self.processType}: {self.expressao()} = {self.__primeiroNum + self.__segundoNum}')
        k.separacao()
    
    def __subtracao(self) -> float:
        k.separacao()
        print(f'{self.processType}: {self.expressao()} = {self.__primeiroNum - self.__segundoNum}')
        k.separacao()
    
    def __multiplicacao(self) -> float:
        k.separacao()
        print(f'{self.processType}: {self.expressao()} = {self.__primeiroNum * self.__segundoNum}')
        k.separacao()

#   a única diferença da divisão é que ela confere se o denumerador da divisão é zero, para que não hajam erros na execução.
    def __divisao(self) -> float:
        k.separacao()
        if self.segundoNumero == 0:
            print(f'{self.processType}: {self.expressao()} = O denumerador desta fração é zero, portanto impossível de se resolver.')
        else:
            print(f'{self.processType}: {self.expressao()} = {self.__primeiroNum / self.__segundoNum}')
        k.separacao()

#   verifica qual operador foi escolhido pelo usuário, chama o método de cálculo referente ao operador escolhido e retorna o valor.
    def execute(self) -> float:
        k.clear()
        match self.__operador:
            case '+': self.__soma()
            case '-': self.__subtracao()
            case '*': self.__multiplicacao()
            case '/': self.__divisao()

#   retorna uma str informando a expressão matemática do objeto.
    def expressao(self) -> str:
        expressao = (f'{self.primeiroNumero} {self.operador} {self.segundoNumero}')
        return expressao
