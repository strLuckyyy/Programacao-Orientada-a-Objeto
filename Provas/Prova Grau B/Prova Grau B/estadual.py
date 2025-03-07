from deputado import Deputado
from funcionario import Funcionario

class Estadual(Deputado):
    def __init__(self, nome: str, partido: str, salarioBruto: float, salarioLiquido: float, funcionarios: list[Funcionario], estado : str) -> None:
        super().__init__(nome, partido, salarioBruto, salarioLiquido, funcionarios)
        self.__estado = estado


