from veiculo import Veiculo

class Aquatico(Veiculo):
    def __init__(self, ano: int, peso: int, tanque: float, modelo: str, qt_motor: int, qt_conves: int) -> None:
        super().__init__(ano, peso, tanque, modelo)
        self.__qt_motor = qt_motor
        self.__qt_conves = qt_conves

    def info(self):
        pass


    def consumo(self):
        #  1/((peso * 0,00002) + (qtMotor * 0,02)), em km/l.
        pass


    def autonomia(self):
        pass
