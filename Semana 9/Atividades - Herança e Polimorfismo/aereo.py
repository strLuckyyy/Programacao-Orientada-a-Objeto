from veiculo import Veiculo

class Aereo(Veiculo):
    def __init__(self, ano: int, peso: int, tanque: float, modelo: str, qt_asa: int, qt_motor: int) -> None:
        super().__init__(ano, peso, tanque, modelo)
        self.__qt_asa = qt_asa
        self.__qt_motor = qt_motor

    #---GETTERS---
    @property
    def get_qt_asa(self):
        return self.__qt_asa
    
    @property
    def get_qt_motor(self):
        return self.__qt_motor
    
    #---SETTERS---
    @get_qt_asa.setter
    def set_qt_asa(self, nova_qt_asa):
        self.__qt_asa = nova_qt_asa
    
    @get_qt_motor.setter
    def set_qt_motor(self, nova_qt_motor):
        self.__qt_motor = nova_qt_motor

    
    def info(self):
        pass


    def consumo(self):
        # 1/((peso * 0,00003) + (qtMotor * 0,01)), em km/l.
        pass


    def autonomia(self):
        pass
