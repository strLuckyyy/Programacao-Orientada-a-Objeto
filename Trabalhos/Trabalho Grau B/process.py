#   Trabalho do Grau B de Programação Orientada a Objetos de Abrahão Francis e Lucas Moraes.

class Process:

#   inicializa os atributos de pid e tipo de processo dos quatro tipos de processos.
    def __init__(self, process : str, pid : int) -> None: 
        self.__process = process
        self.__pid = pid
    
    @property
    def processType(self) -> str:
        return self.__process
    @property
    def pid(self) -> int:
        return self.__pid
    
#   serve apenas para definir que o método execute existe em todos os objetos Process.
    def execute(self):
        pass