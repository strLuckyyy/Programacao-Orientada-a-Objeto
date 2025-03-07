from deputado import Deputado
from funcionario import Funcionario

class Federal(Deputado):
    def __init__(self, nome: str, partido: str, salarioBruto: float, salarioLiquido: float, funcionarios: list[Funcionario], numeroCadastro : int) -> None:
        super().__init__(nome, partido, salarioBruto, salarioLiquido, funcionarios)
        self.__nCadastro = numeroCadastro