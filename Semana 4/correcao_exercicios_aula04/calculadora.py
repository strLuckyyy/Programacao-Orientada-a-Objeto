class Calculadora:
    def __init__(self, cor: str, memoria=0):
        self.__cor = cor
        self.__memoria = memoria

    @property
    def memoria(self):
        return self.__memoria

    @memoria.setter
    def memoria(self, memoria):
        self.__memoria = memoria

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    def soma(self, valor1: float, valor2: float) -> float:
        return valor1 + valor2

    def subtrai(self, valor1: float, valor2: float) -> float:
        return valor1 - valor2

    def multiplica(self, valor1: float, valor2: float) -> float:
        return valor1 * valor2

    def divide(self, valor1: float, valor2: float) -> float:
        if valor2 > 0:
            return valor1 / valor2
        return 0

    def eleva_ao_quadrado(self, valor: int) -> int:
        return valor ** 2

    def eleva_ao_cubo(self, valor: int) -> int:
        return valor ** 3

    def imprime_info(self):
        print("== Dados da calculadora ==")
        print(f"Memória: {self.memoria}\nCor: {self.cor}")
        print("==========================")
