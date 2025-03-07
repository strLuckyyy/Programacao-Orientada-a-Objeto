import os
from pousada import Pousada


#Limpa o terminal 
def clear():
    os.system('cls')

# Espera input do usuário
def wait():
    input('\nPressione Enter para continuar..')
    clear()
   
# Printa todas as opções do menu
def menu():
    print('Escolha uma das seguintes opções usando o número correspondente')
    opção = int(input('1 - Consultar Disponibilidade de um Quarto\n2 - Consultar Reserva de Quarto\n3 - Realizar Uma Reserva\n4 - Cancelar Uma Reserva\n5 - Realizar Check-In de Cliente\n6 - Realizar Check-Out de Cliente\n7 - Registrar Consumo de Cliente\n8 - Salvar Mudanças\n9 - Ver Listas\n0 - Sair do Programa\n\n--> '))
    return opção

# Onde o programa roda até ser fechado
def main():
    clear()
    pousada = Pousada()
    print('Bem vindo ao sistema de gerenciamento da sua pousada!')
    wait()
    clear()
    pousada.infos()
    wait()
    opção_menu = menu()
    while opção_menu != 'end':

    # opção 1 do menu = Consultar Disponibilidade    
        while opção_menu == 1:
            clear()
            pousada.consulta_disponibilidade()
            opção_menu = menu()

    # opção 2 do menu = Consultar Reserva
        while opção_menu == 2:
            clear()
            pousada.consulta_reserva()
            opção_menu = menu()

    # opção 3 do menu = Realizar Reserva
        while opção_menu == 3:
            clear()
            pousada.realiza_reserva()
            opção_menu = menu()
        
    # opção 4 do menu = Cancelar Reserva
        while opção_menu == 4:
            clear()
            pousada.cancela_reserva()
            opção_menu = menu()

    # opção 5 do menu = Realizar Check-In
        while opção_menu == 5:
            clear()
            pousada.realizar_checkin()
            opção_menu = menu()

    # opção 6 do menu = Realizar Check-Out
        while opção_menu == 6:
            clear()
            pousada.realizar_checkout()
            opção_menu = menu()

    # opção 7 do menu = Registrar Consumo
        while opção_menu == 7:
            clear()
            pousada.registrar_consumo()
            opção_menu = menu()

    # opção 8 do menu = Salvar
        while opção_menu == 8:
            clear()
            pousada.salvar_dados()
            opção_menu = menu()

    # opção 9 do menu = Ver Listas
        while opção_menu == 9:
            clear()
            pousada.ver_listas()
            opção_menu = menu()

    # opção 0 do menu = Sair do programa
        while opção_menu == 0:
            clear()
            if int(input('Você gostaria de salvar os dados antes de sair do programa?\n\n1 - Sim\n\n2 - Não\n\n-->')) == 1:
                pousada.salvar_dados()
                opção_menu = 'end'
                clear()
            else:
                opção_menu = 'end'
                clear()
        if 9 < opção_menu or opção_menu < 0:
            clear()
            opção_menu = menu()






if __name__ == '__main__':
    main()