#   Trabalho do Grau B de Programação Orientada a Objetos de Abrahão Francis e Lucas Moraes.

from utility import Utility

k = Utility()

class ProcessQueue:

#   incializa o objeto da fila de processos, que recebe o contador do arquivo 'pid_counter.txt' para nunca repetir um pid.
    def __init__(self):
        self.__fila = []
        with open('pid_counter.txt') as f:
            self.__pidCounter = str(f.read())
        if self.__pidCounter == '':
            self.__pidCounter = 0
        else:
            self.__pidCounter = int(self.__pidCounter)

    @property
    def queue(self):
        return self.__fila
    
    @queue.setter
    def queue(self,newFila):
        self.__fila = newFila

    @property
    def counter(self):
        return self.__pidCounter

    @counter.setter
    def counter(self, new):
        self.__pidCounter = new

#   atualiza o arquivo 'pid_counter.txt' com o último pid utilizado.
    def update_counter(self):
        with open('pid_counter.txt','w') as f:
            f.write(str(self.counter))

#   aumenta o contador de pid e atualiza no arquivo.
    def increase_counter(self):
        self.counter += 1
        self.update_counter()

#   adiciona um processo à fila de processos.
    def add(self, newProcess):
        self.queue.append(newProcess)

#   remove um processo específico da fila.
    def remove(self,removed):
        self.queue.pop(removed)

#   chama o método 'execute' dos objetos da fila, recebendo o index na fila do objeto a ser executado e depois o remove.
    def execute(self, index):
        if self.queue[index].processType == 'Writing Process' or self.queue[index].processType == 'Printing Process' or self.queue[index].processType == 'Reading Process':
            self.queue[index].execute(self)
        else:
            self.queue[index].execute()
        self.remove(index)

#   limpa a fila de todos os processos.
    def clear_queue(self):
        self.queue = []
