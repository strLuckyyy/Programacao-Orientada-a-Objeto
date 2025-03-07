#   Trabalho do Grau B de Programação Orientada a Objetos de Abrahão Francis e Lucas Moraes.

from process import Process
from utility import Utility

k = Utility()

class PrintingProcess(Process):
    
    def __init__(self, pid) -> None:
        super().__init__('Printing Process',pid)

#   método que printa a lista de processos.
    def execute(self,fila) -> None:
        k.separacao()
        print('PID', '\t\t Processo', '\t\tAtributos')
        k.separacao()
        for i in fila.queue:
            if i.processType == 'Computing Process':
                print(f'{i.pid} \t\t {i.processType} \t {i.expressao()}')
            elif i.processType == 'Writing Process':
                print(f'{i.pid} \t\t {i.processType}')
            elif i.processType == 'Reading Process':
                print(f'{i.pid} \t\t {i.processType}')
            elif i.processType == 'Printing Process':
                if len(fila.queue) > 1:
                    print(f'{i.pid} \t\t {i.processType} \t{len(fila.queue)} Processos')
                else:
                    print(f'{i.pid} \t\t {i.processType} \t1 Processo')
        k.separacao()
