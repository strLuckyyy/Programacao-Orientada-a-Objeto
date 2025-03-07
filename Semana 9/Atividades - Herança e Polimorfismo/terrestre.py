from veiculo import Veiculo

class Terrestre(Veiculo):
    def __init__(self, ano: int, peso: int, tanque: float, modelo: str, qt_rodas: int, qt_portas: int) -> None:
        super().__init__(ano, peso, tanque, modelo)
        self.__qt_rodas = qt_rodas
        self.__qt_portas = qt_portas

    #---GETTERS---
    @property
    def get_qt_rodas(self):
        return self.__qt_rodas
    
    @property
    def get_qt_portas(self):
        return self.__qt_portas
    
    #---SETTERS---
    def set_qt_rodas(self, nova_qt_rodas):
        self.__qt_rodas = nova_qt_rodas

    def set_qt_portas(self, nova_qt_portas):
        self.__qt_portas = nova_qt_portas
    

    def info(self):
        consumo = f'{self.consumo():.3f}'
        super().info()
        print(
            ' CONSUMO', '|'.center(27), f'{consumo:>14}',
            '\n AUTONOMIA', '|'.center(23), f'{self.autonomia():>16}',
            '\n QTD PORTAS', '|'.center(22), f'{self.__qt_portas:>16}',
            '\n QTD RODAS', '|'.center(24), f'{self.__qt_rodas:>15}',
            '\n', '-' * 50
        )


    def consumo(self) -> float:
        calculo_consumo = 1 / ((self.get_peso * 0.00005) + (self.__qt_rodas * 0.005)) #em km/l
        return calculo_consumo


    def autonomia(self) -> float:
        
        return 45

