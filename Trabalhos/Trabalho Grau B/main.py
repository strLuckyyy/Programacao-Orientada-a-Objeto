#   Trabalho do Grau B de Programação Orientada a Objetos de Abrahão Francis e Lucas Moraes.

from computing_process import ComputingProcess
from printing_process import PrintingProcess
from utility import Utility
from process_queue import ProcessQueue
from writing_process import WritingProcess
from reading_process import ReadingProcess
import json

k = Utility()
vazia = ('A fila de processos está vazia.')
sucesso = ('Processo criado com sucesso.')

# imprime na tela as opções do menu e retorna a opção.
def menu():
    k.clear()
    op = int(input('O que você deseja fazer?\n1 - Criar Processo\n2 - Executar Próximo\n3 - Executar Processo Específico\n4 - Salvar a Fila de Processos\n5 - Carregar do Arquivo a Fila de Processos\n6 - Sair do Programa\n\n--> '))
    k.clear()
    return op

# responsável pela criação dos processos e adicioná-los à fila de processos.
def criar_processo(fila):
    k.clear()
    check = False
    while check != True:
        k.clear()
        op = int(input('Você deseja criar qual tipo de processo?\n1 - Processo de Cálculo\n2 - Processo de Gravação\n3 - Processo de Leitura\n4 - Processo de Impressão\n5 - Voltar ao menu\n\n--> '))
        if 1 <= op <= 4:
            check = True
        if op == 5:
            break
    k.clear()
    match op:
        case 1:
            primeiroNumero = float(input('Qual o primeiro número do cálculo?\n\n--> '))
            segundoNumero = float(input('Qual o segundo número do cálculo?\n\n--> '))
            op = int(input('Qual operador será usado no cálculo?\n1 - Soma ( + )\n2 - Subtração ( - )\n3 - Multiplicação ( * )\n4 - Divisão ( / )\n\n--> '))
            match op:
                case 1:
                    operador = '+'
                case 2:
                    operador = '-'
                case 3:
                    operador = '*'
                case 4:
                    operador = '/'
            processo = ComputingProcess(primeiroNumero,operador,segundoNumero,fila.counter + 1)
        case 2:
            processo = WritingProcess(fila.counter + 1)
        case 3:
            processo = ReadingProcess(fila.counter + 1)
        case 4:
            processo = PrintingProcess(fila.counter + 1)
        case 5:
            return False
    k.clear()
    return processo

# opção de criação de processos, chama a função 'criar_processos'.
def opcao_menu_1(fila):
    retorno = criar_processo(fila)
    if retorno != False:
        fila.add(retorno)
        k.wait(sucesso)
        fila.increase_counter()
    else:
        k.wait('Nenhum processo foi criado.')

# opção de execução do próximo processo na fila de processos.
def opcao_menu_2(fila):
    if fila.queue == []:
        k.wait(vazia)
    else:
        fila.execute(0)
        k.wait('Processo executado com sucesso')

# opção de execução de um processo específico na fila, que é mostrada através de um objeto PrintingProcess.
def opcao_menu_3(fila):
    if fila.queue == []: 
        k.wait(vazia)
    else:
        end = False
        p = PrintingProcess(0)
        print('Informe o PID do processo que deseja executar da lista abaixo:')
        p.execute(fila)
        print('Digite "0" para voltar.')
        pid = int(input('\n\n--> '))
        for i in range(len(fila.queue)):
            if end == False:
                if fila.queue[i].pid == pid:
                    k.clear()
                    fila.execute(i)
                    k.wait('Processo executado com sucesso.')
                    end = True

# salva a fila de processos com seus PID, tipo de processo e atributos caso existam no arquivo 'lista_processos.txt'.
def opcao_menu_4(fila):
    if fila.queue == []:
        k.wait(vazia)
    else:
        with open('lista_processos.txt') as file:
            reader = json.load(file)
            reader ['queue'] = []
        for i in fila.queue:
            match i.processType:
                case 'Computing Process':
                    proc = {
                        'PID': i.pid,
                        'processType': i.processType,
                        'atributos': [i.primeiroNumero,i.operador,i.segundoNumero]
                    }
                case 'Writing Process':
                    proc = {
                        'PID': i.pid,
                        'processType': i.processType,
                    }
                case 'Reading Process':
                    proc = {
                        'PID': i.pid,
                        'processType': i.processType,
                    }
                case 'Printing Process':
                    proc = {
                        'PID': i.pid,
                        'processType': i.processType
                    }
            reader['queue'].append(proc)
        with open('lista_processos.txt','w') as f:
            json.dump(reader, f)
        k.wait('Fila de processos salva com sucesso.')

# carrega os processos salvos no arquivo 'lista_processos.txt', deletando quaisquer processos na fila atual para que não hajam processos repetidos.
def opcao_menu_5(fila):
    if int(input('Tem certeza que quer fazer isso? A lista atual será apagada.\n1 - Sim\n2 - Não\n\n--> ')) == 1:
        k.clear()
        fila.clear_queue()
        with open('lista_processos.txt') as file:
            reader = json.load(file)
            for i in reader['queue']:
                match i['processType']:
                    case 'Computing Process':
                        primeiroNumero = i['atributos'][0]
                        operador = i['atributos'][1]
                        segundoNumero = i['atributos'][2]
                        pid = i['PID']
                        proc = ComputingProcess(primeiroNumero,operador,segundoNumero,pid)
                    case 'Writing Process':
                        pid = i['PID']
                        proc = WritingProcess(pid)
                    case 'Reading Process':
                        pid = i['PID']
                        proc = ReadingProcess(pid)
                    case 'Printing Process':
                        pid = i['PID']
                        proc = PrintingProcess(pid)
                fila.add(proc)
        reader['queue'] = []
        k.wait('Fila de processos carregada com sucesso.')
        with open('lista_processos.txt','w') as f:
            json.dump(reader, f)

# roda apenas as opções do menu
def main():
    fila = ProcessQueue()
    k.clear()
    opMenu = 'n'
    while opMenu != 0:
        opMenu = menu()
        match opMenu:
            case 1:
                opcao_menu_1(fila)
            case 2:
                opcao_menu_2(fila)
            case 3:
                opcao_menu_3(fila)
            case 4:
                opcao_menu_4(fila)
            case 5:
                opcao_menu_5(fila)
            case 6:
                fila.update_counter()
                quit()

if __name__ == '__main__':
    main()
