#   Trabalho do Grau B de Programação Orientada a Objetos de Abrahão Francis e Lucas Moraes.

from process import Process
from utility import Utility
from computing_process import ComputingProcess
import json

k = Utility()

class ReadingProcess(Process):

#   iniciliazia o processo de leitura recebendo um 'pid' da fila de processos e definindo seu tipo para 'Reading Process' dentro da sua superclasse.
    def __init__(self, pid) -> None:
        super().__init__('Reading Process',pid)
    
#   executa o processo ReadingProcess, que recebe a fila de processos como parâmetro, lendo o dicionário no arquivo 'computation.txt',
#   criando um processo ComputingProcess e adicionando-o na fila de processos. isso acontece para cada processo salvo no arquivo.
#   após isso o arquivo é limpo para que não possam existir processos iguais dentro dele.
    def execute(self,fila):
        with open('computation.txt') as file:
            reader = (json.load(file))
        if reader['processes'] != []:
            for i in reader['processes']:
                fila.increase_counter()
                primeiroNumero = i['atributos'][0]
                operador = i['atributos'][1]
                segundoNumero = i['atributos'][2]
                proc = ComputingProcess(primeiroNumero,operador,segundoNumero,fila.counter)
                fila.add(proc)
            with open('computation.txt','w') as f:
                dump = reader
                dump ['processes'] = []
                json.dump(dump,f)
            k.wait('Arquivo carregado com sucesso.')
        else:
            k.wait('O arquivo está vazio.')
        

