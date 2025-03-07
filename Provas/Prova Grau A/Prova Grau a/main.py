from animal import Animal
from fazenda import Fazenda
import os

def wait(): 
    input('Aperte ENTER para continuar...')
    os.system('cls')


def main():

    wait()

    porco = Animal('Jaiminho', 'Suíno', 100.0, 5)
    galinha = Animal('Pica-Pica', 'Ave', 10, 3)

    fazenda_do_galo_cego = Fazenda()

    fazenda_do_galo_cego.adicionar_animal(porco)
    fazenda_do_galo_cego.adicionar_animal(galinha)

    bicho = Animal(input('Qual o nome do animal? '), input('Qual tipo do animal? '), float(input('Qual o peso do animal? ')), int(input('Qual a idade do animal? ')))
    fazenda_do_galo_cego.adicionar_animal(bicho)

    wait()

    media = fazenda_do_galo_cego.idade_media()
    valor_total = fazenda_do_galo_cego.calcular_valor_animais()

    print('-' * 50)
    print(f'A média de idade entre os animais da fazenda é: {media:.2f}')
    print(f'O valor de venda total dos animais da fazenda é: {valor_total:.2f}')
    print('-' * 50)

    lista_animais = fazenda_do_galo_cego.animais

    for animais in lista_animais: print(f'O animal {animais.nome} é do tipo {animais.tipo}')
    print('-' * 50)

    nome = input('Digite o nome de um animal da fazenda: ')

    result = fazenda_do_galo_cego.aumenta_idade(nome)

    if result == True: print('Idade aumentada em +1 com sucesso')
    else: print('Não foi possivel localizar o animal. Tente novamente mais tarde!')
    
    wait()

    fazenda_do_galo_cego.imprimi_info()


if __name__ == '__main__':
    main()
