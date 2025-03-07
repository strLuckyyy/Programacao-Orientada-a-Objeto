'''
Crie uma classe chamada Pessoa. Uma pessoa possui nome, idade, altura,
quantidade de irmãos e endereço. Na classe Pessoa: 
• crie um método chamado imprime_info, que imprime na tela as informações
da pessoa, de maneira organizada.
• crie um método chamado is_filho_unico, que retorna verdadeiro caso a
pessoa seja filha única e falso caso contrário.
No método main() faça o que se pede:
• crie 3 pessoas informando todos os dados.
• imprima as informações de todas as pessoas, de forma legível e organizada.
• imprima na tela a frase “Filho(a) único(a)” ou “Filhs únics” para as pessoas que
forem filhas únicas, e a frase “Não é filho(a) único(a)” ou “Não é filhs únics” para
as pessoas que não forem filhas únicas
'''

import os

class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float, irmaos: int, endereco: str) -> None:
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.qtdIrmaos = irmaos
        self.endereco = endereco


    def imprime_info(self, cadastro):
        print(f'Ficha:\n',
              f'-' * 50, '\n'
              f'\tNome\t\t\t|\t{cadastro[0]}\n',
              f'\tIdade\t\t\t|\t{cadastro[1]}\n',
              f'\tAltura\t\t\t|\t{cadastro[2]}\n',
              f'\tQuantidade de Irmãos\t|\t{cadastro[3]}\n',
              f'\tEndereço\t\t|\t{cadastro[4]}\n')
        
    
    def is_filho_unico(self, irmaos):
        if irmaos > 0:
            return False
        else:
            return True


def cadastro():

    '''
    0 nome
    1 idade
    2 altura
    3 irmao
    4 endereco
    '''

    i = []

    print('-' * 15, '\n')
    i.append(input('Qual o nome da pessoa? '))
    i.append(int(input('Qual a idade da pessoa? ')))
    i.append(float(input('Qual a altura da pessoa? ')))
    i.append(int(input('Quantos irmãos a pessoa possuí? ')))
    i.append(input('Qual o endereço da pessoa? '))
    print('\n')

    return i


def decIrmaos(pessoa, cadastro):
    if pessoa.is_filho_unico(cadastro[3]) == True:
        print(f'{cadastro[0]} é filho(a) único(a)')
        return
    else:
        print(f'{cadastro[0]} tem {cadastro[3]} irmãos(ãs)')
        return
    

def main():
    os.system('cls')

    i1 = cadastro()
    i2 = cadastro()
    i3 = cadastro()

    Pessoa1 = Pessoa(i1[0], i1[1], i1[2], i1[3], i1[4])
    Pessoa2 = Pessoa(i2[0], i2[1], i2[2], i2[3], i2[4])
    Pessoa3 = Pessoa(i3[0], i3[1], i3[2], i3[3], i3[4])

    Pessoa1.imprime_info(i1)
    decIrmaos(Pessoa1, i1)
    print()
    Pessoa2.imprime_info(i2)
    decIrmaos(Pessoa2, i2)
    print()
    Pessoa3.imprime_info(i3)
    decIrmaos(Pessoa3, i3)
    print()

if __name__ == '__main__':
    main()