'''
Classe Calculadora:
◦ Uma calculadora possui uma memória e uma cor.
◦ Quando uma calculadora é criada, a memória deve ser inicializada com 0 e a cor
deve ser recebida por parâmetro (construtor).
◦ Crie os métodos de acesso para os atributos da classe (get e set).
◦ Crie os métodos: soma, subtrai, multiplica e divide. Todos recebem dois
valores (float) por parâmetro e retornam o valor da operação realizada.
◦ Crie os métodos eleva_ao_quadrado e eleva_ao_cubo. Ambos recebem
apenas um valor (int) e retornam o valor da operação realizada.
◦ Crie um método imprime_info, que não recebe parâmetros e simplesmente
imprime as informações da calculadora de maneira legível e organizada.
'''
from ficha import Ficha



class Calculadora:
    def __init__(self, color: str, memory: int = 0):
        self.__color = color
        self.__memory = memory


    @property
    def memory(self):
        return self.__memory
    

    @memory.setter
    def memory(self, memory):
        self.__memory = memory

    
    @property
    def color(self):
        return self.__color
    

    @color.setter
    def color(self, color):
        self.__color = color


    def soma(self, value_1: float, value_2: float) -> float:
        total: float = 0.0
        total = value_1 + value_2
        return total
    

    def subtracao(self, value_1: float, value_2: float) -> float:
        total: float = 0.0
        total = value_1 - value_2
        return total


    def divisao(self, value_1: float, value_2: float) -> float:
        total: float = 0.0
        total = value_1 / value_2
        return total
    

    def multip(self, value_1: float, value_2: float) -> float:
        total: float = 0.0
        total = value_1 * value_2
        return total
    

    # Simplifiquei?
    def potenciacao(self, value_1: float, expoente: int = 2) -> int:
        total: int = 0
        total = int(value_1 ** expoente)
        return total


    def imprime_info(self):
        nome: list = ['Cor', 'Memória']
        valor: list = [self.__color, self.__memory]

        info = Ficha('INFORMAÇÕES DA CALCULADORA')

        info.titulo()
        info.conteudo(nome, valor)
