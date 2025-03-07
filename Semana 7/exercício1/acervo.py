from usuario import Usuario
from livro import Livro
import os


class Acervo: 
    def __init__(self, livros : list) -> None:
        self.__livros = livros


#   GET & SET   #
    @property
    def livros(self) -> list:
        return self.__livros
    
    @livros.setter
    def livros(self, novosLivros : list) -> None:
        self.__livros = novosLivros
#   ---------   #


#   Referente a lista de livros na biblioteca
    def consultarAcervo(self):
        n = 1
        for i in self.__livros:
            print(f'| {n}\t| {i.titulo} \t| {i.qtdDisponivel} exemplares disponiveís', end='\n\n')
            n += 1

#   Referente a locação dos livros
    def solicitarEmprestimo(self, user : Usuario):
        self.consultarAcervo()
        index = int(input('\nQual o número do livro que você deseja locar? ')) - 1
        livro = self.__livros[index]
        confi = input(f'\nConfirma a escolha do livro {livro.titulo}? (s/n)')

        if confi.lower() == 's':
            disponibilidade = livro.consultarDisponibilidade()
            if disponibilidade == True: #   Caso a disponibilidade seja True, a locação será continuada. Caso seja False, o código da a opção de reserva.
                quantidade = int(input('\nDeseja quantos exemplares? '))
                verificacao = user.emprestimo(livro, quantidade)

                if verificacao == False: #  Não houve locação, logo volte para o menu
                    return
                elif verificacao == True: #    Houve locação parcial, logo subtraia do disponível e coloque na estante
                    livro.qtdDisponivel -= quantidade
                    if livro.qtdDisponivel <= 0: livro.qtdDisponivel = 0
                    user.imprimeEstante()
                    return
                    
                self.solicitarReserva(verificacao) #    Referente ao "return reserva", indica que houve uma locação completa e uma reserva em nome do user
                livro.qtdDisponivel = 0
                user.imprimeEstante()
                return
            
            elif disponibilidade == False: #    Reserva
                escolha = input('Deseja marcar reserva? s/n')
                match escolha.lower():
                    case 's':
                        self.solicitarReserva(livro, user, int(input('Quantos exemplares deseja reservar? ')))
                    case 'n':
                        return
        else:
            os.system('cls')
            self.solicitarEmprestimo(user) #    Loop de mentirinha

#   Referente a reserva de um livro
    def solicitarReserva(self, livro : Livro, user : Usuario, quantidade : int):
        reservaUser = user.reservas
        reservaUser.append([quantidade, livro])
        user.reservas = reservaUser

#   Referente a colocação de livros no acervo
    def adicionarLivros(self, livro : Livro):
        self.__livros.append(livro)

#   Referente a exclução do livro do acervo
    def removerLivro(self):
        self.consultarAcervo()

        index = int(input('\nQual o número do livro? \n -> ')) - 1
        self.__livros.pop(index)
        os.system('cls')

        self.consultarAcervo()

#   Referente a devolução dos livros
    def devolverLivros(self, user : Usuario, livro : Livro, quantidade : int):
        user.devolverLivro(livro, quantidade)

#   Referente ao "Relatório Local"
    def relatorio(self, user : Usuario):
        print('-' * 50, end='\n')
        print(f'Quantidade de Livros no Acervo: \t| {len(self.__livros)}\n')
        print(f'Exemplares emprestados ao {user.nome} \t| {len(user.estante)}\n')
        print(f'Exemplares reservados ao {user.nome} \t| {len(user.reservas)}\n')
        print('-' * 50)
