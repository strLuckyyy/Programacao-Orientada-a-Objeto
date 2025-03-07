class Funcionario:
    def __init__(self, nome, salarioBruto, salarioLiquido) -> None:
        self.__nome = nome
        self.__salarioBruto = salarioBruto
        self.__salarioLiquido = salarioLiquido
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def salarioBruto(self):
        return self.__salarioBruto
    
    @property
    def salarioLiquido(self):
        return self.__salarioLiquido
    
    
