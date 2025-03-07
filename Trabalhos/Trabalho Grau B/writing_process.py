#   Trabalho do Grau B de Programação Orientada a Objetos de Abrahão Francis e Lucas Moraes.

from process import Process
from utility import Utility
import json

k = Utility()

class WritingProcess(Process):
    
#   iniciliazia o processo de gravação recebendo um 'pid' da fila de processos e definindo seu tipo para 'Writing Process' dentro da sua superclasse
    def __init__(self, pid) -> None:
        super().__init__('Writing Process',pid)
    
#   executa o processo WritingProcess, sobescrevendo o processo da superclasse para salvar no arquivo 'computation.txt'
#   como um dicionário os processos de computação presentes na fila de processo, salvando apenas seus atributos.
    def execute(self,fila):
        with open('computation.txt') as f:
            reader = (json.load(f))
        for i in fila.queue:
            if i.processType == 'Computing Process':
                proc = {
                    'atributos': [i.primeiroNumero,i.operador,i.segundoNumero]
                }
                reader['processes'].append(proc)
        with open('computation.txt','w') as f:
            json.dump(reader,f)
        if reader['processes'] == []:
            k.wait('Não há processos de computação para serem salvos.')
        else:
            k.wait('Arquivo salvo com sucesso.')

