import os
import json
from reserva import Reserva
from quarto import Quarto
from produto import Produto

def clear():
    os.system('cls')

def wait():
    input('\nPressione Enter para continuar..')
    clear()

def zero_placer(var):
    x = '0'
    x += var
    return x

def decode_data(data):
    Dat = ''
    Dat += data[2]
    Dat += data[3]
    Dat += '/'
    Dat += data[0]
    Dat += data[1]
    return Dat

def formalize_obj_quarto(obj):
    x = {
        "numero":obj.get_numero(),
        "categoria":obj.get_categoria_fim(),
        "diaria":obj.get_diaria(),
        "consumo":obj.get_consumo()
    }
    return x

def formalize_obj_reserva(obj):
    x = {
        "data_inicio":obj.get_data_inicio(),
        "data_fim":obj.get_data_final(),
        "cliente":obj.get_cliente(),
        "numero_quarto":obj.get_num_quarto(),
        "status":obj.get_status()
    }
    return x

def formalize_obj_produto(obj):
    x = {
        "codigo":obj.get_codigo(),
        "nome":obj.get_nome(),
        "preco":obj.get_preco()
    }
    return x

class Pousada:
# inicializa o objeto pousada
    def __init__(self):
        self.arq_pousada = self.carregar_dados('pousada')
        self.__nome = self.arq_pousada['nome']
        self.__contato = self.arq_pousada['contato']
        self.__quartos = self.inicializar_quartos()
        self.__reservas = self.inicializar_reservas()
        self.__produtos = self.inicializar_produtos()
# carrega dados do arquivo selecionado
    def carregar_dados(self,file_name):
        f = open(f'{file_name}.txt')
        dados = json.load(f)
        return dados
# salva os dados do arquivo selecionado
    def salvar_dados(self):
        dados = self.carregar_dados('pousada')
        with open(f'pousada.txt','w') as f:
            dados['nome'] = self.__nome
            dados['contato'] = self.__contato
            json.dump(dados,f)

        dados = self.carregar_dados('quarto')
        with open(f'quarto.txt','w') as f:
            dicionario = []
            for i in range(len(self.get_quartos())):
                dicionario.append(formalize_obj_quarto(self.get_quartos()[i]))
            dados['quartos'] = dicionario
            json.dump(dados,f)

        dados = self.carregar_dados('reserva')
        with open(f'reserva.txt','w') as f:
            dicionario = []
            for i in range(len(self.get_reservas())):
                dicionario.append(formalize_obj_reserva(self.get_reservas()[i]))
            dados['reservas'] = dicionario
            json.dump(dados,f)

        dados = self.carregar_dados('produto')
        with open(f'produtos','w') as f:
            dicionario = []
            for i in range(len(self.get_produtos())):
                dicionario.append(formalize_obj_produto(self.get_produtos()[i]))
            dados['produtos'] = dicionario
            json.dump(dados,f)
        

        clear()
        print('Seus dados foram salvos!')
        wait()
# retorna o nome da pousada
    def get_nome(self):
        return self.__nome
# retorna o contato da pousada
    def get_contato(self):
        return self.__contato
# retorna a lista de objetos Quarto
    def get_quartos(self):
        return self.__quartos
# retorna a lista de objetos Reserva
    def get_reservas(self):
        return self.__reservas
# adiciona a reserva na lista de Objeto
    def adicionar_reserva(self,data_inicio,data_fim,cliente,numero_quarto):
        lista_reservas = self.get_reservas()
        lista_reservas.append(Reserva(data_inicio,data_fim,cliente,numero_quarto,'a'))
        self.set_reservas(lista_reservas)
        print(f'A reserva de {cliente} do quarto {numero_quarto} para o dia {decode_data(data_inicio)} foi feita com sucesso!')
        wait()
# retorna a lista de objetos Produto
    def get_produtos(self):
        return self.__produtos
# define o nome da pousada
    def set_nome(self,nome):
        self.__nome = nome
# define o contato da pousada
    def set_contato(self,contato):
        self.__contato = contato
# define a lista de objetos Quarto
    def set_quartos(self,quartos):
        self.__quartos = quartos 
# define a lista de objetos Reserva
    def set_reservas(self,reservas):
        self.__reservas = reservas 
# define a lista de objetos Produto
    def set_produtos(self,produtos):
        self.__produtos['produtos'] = produtos 
# limpa a lista de objetos Produto
    def limpar_produtos(self):
        self.__produtos = []
# printa as infos
    def infos(self):
        print(f'As informações sobre sua pousada são as seguintes:\n\nNome da Pousada: {self.get_nome()}\nContato da Pousada: {self.get_contato()}\nA Pousada tem {len(self.get_quartos())} Quartos\nReservas Ativas: {len(self.get_reservas())}\nProdutos Disponíveis: {len(self.get_produtos())}')
# busca se alguma variável está em uma lista
    def check_if_in_list(self,search,listing):
        for i in range(len(listing)):
            if search == listing[i].get_cliente():
                return True
        return False
# busca se um quarto está reservado
    def check_is_room_booked(self,data_inicio,data_final,room):
        lista_quartos = self.get_reservas()
        for i in range(len(lista_quartos)):
            if room == lista_quartos[i].get_num_quarto():
                inicio_reserva = lista_quartos[i].get_data_inicio()
                fim_reserva = lista_quartos[i].get_data_final()
                if inicio_reserva <= data_inicio <= fim_reserva or inicio_reserva <= data_final <= fim_reserva:
                    print(f'O quarto {room} já está reservado com data de início {decode_data(inicio_reserva)} e data de saída {decode_data(fim_reserva)}')
                    wait()
                    return True
                if data_inicio < inicio_reserva and fim_reserva < data_final:
                    print(f'O quarto {room} já está reservado com data de início {decode_data(inicio_reserva)} e data de saída {decode_data(fim_reserva)}')
                    wait()
                    return True
        return False

    def realiza_reserva(self):
        lista_quartos = self.get_quartos()
        etapa = 'nome'
        while etapa == 'nome':
            nome_cliente = input('Qual o nome do cliente?\n\n--> ')
            nome_cliente = nome_cliente.capitalize()
            if self.check_if_in_list(nome_cliente,self.get_reservas()) == False:
                etapa = 'quarto'
            else:
                print('Esse cliente já tem uma reserva ativa')
                wait()
        while etapa == 'quarto':
            clear()
            num_quarto = int(input('Qual o número do quarto da reserva?\n\n--> '))
            if num_quarto > len(lista_quartos):
                print(f'O quarto selecionado não existe, selecione um quarto de 1 a {len(lista_quartos)}')
                wait()    
            else:
                etapa = 'data'
        while etapa == 'data':
            clear()
            dia_inicio = str(input('Qual o dia de início da reserva?\n\n--> '))
            if len(dia_inicio) == 1:
                dia_inicio = zero_placer(dia_inicio)
            clear()
            mes_inicio = str(input('Qual o mês de inicio da reserva?\n\n--> '))
            if len(mes_inicio) == 1:
                mes_inicio = zero_placer(mes_inicio)
            data_inicio = mes_inicio + dia_inicio
            clear()
            dia_final = str(input('Qual o dia de encerramento da reserva?\n\n--> '))
            if len(dia_final) == 1:
                dia_final = zero_placer(dia_final)
            clear()
            mes_final = str(input('Qual o mês de encerramento de reserva?\n\n--> '))
            if len(mes_final) == 1:
                mes_final = zero_placer(mes_final)
            data_final = mes_final + dia_final
            clear()
            if int(data_final) <= int(data_inicio):
                print('A data de encerramento da reserva deve ser após o início da reserva')
                wait()
            else:
                if self.check_is_reserve_active(num_quarto,nome_cliente) == False:   
                    if self.check_is_room_booked(data_inicio,data_final,num_quarto) == True:
                        clear()
                    else:
                        self.adicionar_reserva(data_inicio,data_final,nome_cliente,num_quarto)
                        clear()
                        etapa = 'end'
# busca se uma reserva está ativa
    def check_is_reserve_active(self,room,nome):
        encontrado = False
        lista_reservas = self.get_reservas()
        for i in range(len(lista_reservas)):
            if lista_reservas[i].get_cliente() == nome:
                if lista_reservas[i].get_status() != 'a' or lista_reservas[i].get_status() != 'i':
                    if room == int(lista_reservas[i].get_num_quarto()):
                        encontrado = False
                else:
                    return True
        return encontrado

    def cancela_reserva(self):
        a = False
        cliente = str(input('A reserva está em qual nome?\n\n--> '))
        cliente = cliente.capitalize()
        lista_reservas = self.get_reservas()
        for i in range(len(lista_reservas)):
            if lista_reservas[i].get_cliente() == cliente:
                lista_reservas[i].cancela_reserva()
                self.set_reservas(lista_reservas)
                clear()
                print('Reserva cancelada com sucesso!')
                a = True
                wait()
        if a == False:
            print('Não existe reserva no nome desse cliente')
            wait()
        clear()

    def consulta_disponibilidade(self):
        datas = self.pede_data()
        clear()
        room = input('Qual o número do quarto?\n\n--> ')
        if self.check_is_room_booked(datas[0],datas[1],room)== False:
            print(f'O quarto {room} está livre na data {decode_data(datas[0])} até {decode_data(datas[1])}')
            wait()

    def consulta_reserva(self):
        datas = 0
        nome = 0
        room = 0
        if int(input('Você sabe as datas da reserva a ser consultada?\n\n1 - Sim\n\n2 - Não\n\n--> ')) == 1:
            clear()
            datas = self.pede_data()
        clear()
        if int(input('Você sabe o nome do cliente da reserva a ser consultada?\n\n1 - Sim\n\n2 - Não\n\n--> ')) == 1:
            clear()
            nome = input('Qual o nome do cliente?\n\n--> ').capitalize()
        clear()
        if int(input('Você sabe o número do quarto da reserva a ser consultada?\n\n1 - Sim\n\n2 - Não\n\n--> ')) == 1:
            clear()
            room = input('Qual o número do quarto?\n\n--> ')
        lista_reservas = self.get_reservas()
        lista_quartos = self.get_quartos()
        index = []
        found = False
        if nome != 0:
            for i in range(len(lista_reservas)):
                if nome == lista_reservas[i].get_cliente():
                    index.append(i)
                    found = True
        if datas != 0:
            for i in range(len(lista_reservas)):
                if datas[0] == lista_reservas[i].get_data_inicio() and datas[1] == lista_reservas[i].get_data_final():
                    index.append(i)
                    found = True
        if room != 0:
            for i in range(len(lista_reservas)):
                if room == lista_reservas[i].get_num_quarto():
                    index.append(i)
                    found = True
        if found == True:
            clear()
            historico = []
            for i in range(len(index)):
                if lista_reservas[index[i]] not in historico:
                    print('As reservas com dados iguais aos informados são as seguintes:\n')
                    lista_reservas[index[i]].imprime_infos()
                    print('\n-As informações do quarto são as seguintes:\n')
                    lista_quartos[int(lista_reservas[index[i]].get_num_quarto())-1].imprime_infos()
                    historico.append(index[i])
                    wait()
                
                    
        else:
            print('Não existe uma reserva com as informações entregues')
            wait()

    def realizar_checkin(self):
        lista_reservas = self.get_reservas()
        lista_quartos = self.get_quartos()
        found = False
        nome = input('Qual o nome do cliente?\n\n--> ').capitalize()
        for i in range(len(lista_reservas)):
            if nome == lista_reservas[i].get_cliente():
                found = True
                if lista_reservas[i].get_status() == 'a':
                    lista_reservas[i].fazer_check_in()
                    self.set_reservas(lista_reservas)
                    quant_dias = int(lista_reservas[i].get_data_final()) - int(lista_reservas[i].get_data_inicio())
                    clear()
                    print(f'O cliente {lista_reservas[i].get_cliente()} ficará hospedado no quarto {lista_reservas[i].get_num_quarto()} a partir de {decode_data(lista_reservas[i].get_data_inicio())} até {decode_data(lista_reservas[i].get_data_final())}, totalizando {quant_dias} dias')
                    wait()
                    print(f'Valor total das diárias: R${quant_dias*int(lista_quartos[int(lista_reservas[i].get_num_quarto())-1].get_diaria())}')
                    wait()
                    print(f'Dados do quarto:\n')
                    lista_quartos[int(lista_reservas[i].get_num_quarto())-1].imprime_infos()
                    wait()
                elif lista_reservas[i].get_status() == 'i':
                    print('O cliente já fez o check-in')
                    wait()
                elif lista_reservas[i].get_status() == 'o':
                    print('O cliente já fez o check-out')
                    wait()
                elif lista_reservas[i].get_status() == 'c':
                    print('A reserva do cliente foi cancelada')
                    wait()
        if found == False:
            print('Nenhuma reserva ativa com esse nome foi encontrada')
            wait()

    def realizar_checkout(self):
        lista_reservas = self.get_reservas()
        lista_quartos = self.get_quartos()
        lista_produtos = self.get_produtos()
        valor_consumos = 0
        found = False
        nome = input('Qual o nome do cliente?\n\n--> ').capitalize()
        for i in range(len(lista_reservas)):
            if nome == lista_reservas[i].get_cliente():
                if lista_reservas[i].get_status() == 'i':
                    found = True
                    num_quarto = int(lista_reservas[i].get_num_quarto())
                    lista_consumo = lista_quartos[num_quarto-1].get_consumo()
                    for c in range(len(lista_consumo)):
                        for p in range(len(lista_produtos)):
                            if lista_consumo[c] == lista_produtos[p].get_codigo():
                                valor_consumos += float(lista_produtos[p].get_preco())
                    lista_reservas[i].fazer_check_out()
                    lista_quartos[num_quarto-1].limpa_consumo()
                    self.set_reservas(lista_reservas)
                    quant_dias = int(lista_reservas[i].get_data_final()) - int(lista_reservas[i].get_data_inicio())
                    valor_diaria = quant_dias*int(lista_quartos[num_quarto-1].get_diaria())
                    clear()
                    print(f'O cliente {lista_reservas[i].get_cliente()} ficou hospedado no quarto {num_quarto} de {decode_data(lista_reservas[i].get_data_inicio())} até {decode_data(lista_reservas[i].get_data_final())}, totalizando {quant_dias} dias')
                    wait()
                    print(f'Valor total das diárias: R${valor_diaria}\nValor total do consumo: R${valor_consumos}\nValor total a ser pago: R${valor_diaria+valor_consumos}')
                    wait()
                    print(f'Dados do quarto:\n')
                    lista_quartos[int(num_quarto-1)].imprime_infos()
                    wait()
        if found == False:
            print('Nenhuma reserva ativa com esse nome foi encontrada')
            wait()

    def registrar_consumo(self):
        lista_reservas = self.get_reservas()
        lista_produtos = self.get_produtos()
        lista_quartos = self.get_quartos()
        reserva = False
        num = int(input('Qual o número do quarto?\n\n--> '))
        if int(len(lista_quartos)) < num or num < 1:
            print(f'\nNão existe quarto de número {num}')
            wait()
            reserva = True
        for i in range(len(lista_reservas)):
            if lista_reservas[i].get_num_quarto() == num and lista_reservas[i].get_status() == 'i':
                reserva = True
                clear()
                for i in range(len(lista_produtos)):
                    lista_produtos[i].imprime_infos()
                    print()
                produto = input(f'Digite o nome do produto:\n\n--> ').lower()
                found = False
                for i in range(len(lista_produtos)):
                    if produto == lista_produtos[i].get_nome():
                        found = True
                        lista_quartos[num-1].adiciona_consumo(int(lista_produtos[i].get_codigo()))
                if found == False:
                    print('Nenhum produto com o código informado foi encontrado')
                    wait()
        if reserva == False:
            print(f'Não existe reserva ativa no quarto de número {num}')
            wait()
        clear()
# inicializa os objetos a partir dos arquivos
    def inicializar_quartos(self):
        arq = self.carregar_dados('quarto')
        arq = arq['quartos']
        lista_obj = []
        for l in range(len(arq)):
            lista_obj.append(Quarto(arq[l]['numero'],arq[l]['categoria'],arq[l]['diaria'],arq[l]['consumo']))
        return lista_obj

    def inicializar_reservas(self):
        arq = self.carregar_dados('reserva')
        arq = arq['reservas']
        lista_obj = []
        for l in range(len(arq)):
            lista_obj.append(Reserva(arq[l]['data_inicio'],arq[l]['data_fim'],arq[l]['cliente'],arq[l]['numero_quarto'],arq[l]['status']))
        return lista_obj

    def inicializar_produtos(self):
        arq = self.carregar_dados('produto')['produtos']
        lista_obj = []
        for l in range(len(arq)):
            lista_obj.append(Produto(arq[l]['codigo'],arq[l]['nome'],arq[l]['preco']))
        return lista_obj
# pede uma data de início e fim para uma reserva
    def pede_data(self):
        datas = []
        etapa = 'data'
        while etapa == 'data':
            dia = input('Qual o dia do início?\n\n--> ')
            if len(dia) == 1:
                dia = zero_placer(dia)
            clear()
            mês = input('Qual o mês de início?\n\n--> ')
            if len(mês) == 1:
                mês = zero_placer(mês)
            clear()
            data_inicio = mês + dia
            datas.append(data_inicio)
            dia = input('Qual o dia de fim?\n\n--> ')
            if len(dia) == 1:
                dia = zero_placer(dia)
            clear()
            mês = input('Qual o mês de fim?\n\n--> ')
            if len(mês):
                mês = zero_placer(mês)
            clear()
            data_final = mês + dia
            datas.append(data_final)
            if int(data_final) <= int(data_inicio):
                print('A data de encerramento da reserva deve ser após o início da reserva')
                wait()
            else:
                etapa = 'end'
        return datas
# mostra as listas de reservas, quartos ou produtos
    def ver_listas(self):
        opção = int(input('Você deseja ver qual lista?\n1 - Reservas\n2 - Quartos\n3 - Produtos\n\n--> '))
        clear()
        if opção == 1:
            lista = self.get_reservas()
            for i in range(len(lista)):
                print(f'Há um total de {len(lista)} reservas\n')
                lista[i].imprime_infos()
                wait()
        elif opção == 2:
            lista = self.get_quartos()
            for i in range(len(lista)):
                print(f'Há um total de {len(lista)} quartos\n')
                lista[i].imprime_infos()
                wait()
        elif opção == 3:
            lista = self.get_produtos()
            for i in range(len(lista)):
                print(f'Há um total de {len(lista)} produtos\n')
                lista[i].imprime_infos()
                wait()
        else:
            print('Nenhuma opção válida selecionada, retornando ao menu')
            wait()



