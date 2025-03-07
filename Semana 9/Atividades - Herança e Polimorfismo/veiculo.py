class Veiculo:
    def __init__(self, ano: int, peso: int, tanque: float, modelo: str) -> None:
        self.__ano = ano
        self.__peso = peso
        self.__tanque = tanque
        self.__modelo = modelo
    
    #---GETTERS---
    @property
    def get_ano(self):
        return self.__ano
    
    @property
    def get_peso(self):
        return self.__peso
    
    @property
    def get_tanque(self):
        return self.__tanque
    
    @property
    def get_modelo(self):
        return self.__modelo
    
    #---SETTERS---
    @get_ano.setter
    def set_ano(self, novo_ano):
        self.__ano = novo_ano
    
    @get_peso.setter
    def set_peso(self, novo_peso):
        self.__peso = novo_peso
    
    @get_tanque.setter
    def set_tanque(self, novo_tanque):
        self.__tanque = novo_tanque
    
    @get_modelo.setter
    def set_modelo(self, novo_modelo):
        self.__modelo = novo_modelo
    

    def info(self):
        print(
            '\n', '-' * 50,
            '\n INFORMAÇÃO DO VEÍCULO'.center(50),
            '\n', '-' * 50,
            '\n MODELO', '|'.center(30), f'{self.__modelo:>12}',
            '\n ANO', '|'.center(35), f'{self.__ano:>10}',
            '\n CAPACIDADE DO TANQUE', '|', f'{self.__tanque:>27}',
            '\n PESO', '|'.center(34), f'{self.__peso:>10}'
            '\n', '-' * 50
        )
