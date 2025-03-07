from calculadora import Calculadora


class FuncionarioCaixa:
    def __init__(self, nome: str, endereco: str, calculadora: Calculadora):
        self.__nome = nome
        self.__endereco = endereco
        self.__calculadora = calculadora

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def calculadora(self):
        return self.__calculadora

    @calculadora.setter
    def calculadora(self, calculadora):
        self.__calculadora = calculadora

    def soma(self, valor1: float, valor2: float) -> float:
        return self.calculadora.soma(valor1, valor2)

    def subtrai(self, valor1: float, valor2: float) -> float:
        return self.calculadora.subtrai(valor1, valor2)

    def multiplica(self, valor1: float, valor2: float) -> float:
        return self.calculadora.multiplica(valor1, valor2)

    def divide(self, valor1: float, valor2: float) -> float:
        return self.calculadora.divide(valor1, valor2)

    def eleva_ao_quadrado(self, valor: int) -> int:
        return self.calculadora(valor)

    def eleva_ao_cubo(self, valor: int) -> int:
        return self.calculadora(valor)

    def imprime_info(self):
        print("---- Dados do Funcionário ----")
        print(f"Nome: {self.nome}\nEndereço: {self.endereco}")
        self.calculadora.imprime_info()
        print("------------------------------")
