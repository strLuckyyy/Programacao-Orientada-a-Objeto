class Deputado:
    def __init__(self, nome : str, partido : int, salarioBruto : float, salarioLiquido : float, funcionarios : list) -> None:
        self.__nome = nome
        self.__partido = partido
        self.__salarioBruto = salarioBruto
        self.__salarioLiquido = salarioLiquido
        self.__funcionarios = funcionarios

    @property
    def nome(self):
        return self.__nome
    
    @property
    def partido(self):
        return self.__partido
    
    @property
    def salarioBruto(self):
        return self.__salarioBruto
    
    @property
    def salarioLiquido(self):
        return self.__salarioLiquido

    @property
    def funcionarios(self):
        return self.__funcionarios
    

#   TypeError: object of type 'int' has no len()
    def numero_funcionarios(self):
        numero = 0
        for i in range(self.__funcionarios):
            numero += 1
        return numero

