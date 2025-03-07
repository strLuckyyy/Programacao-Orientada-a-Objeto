from livro import Livro

class Usuario:
    def __init__(self, nome : str, estante : list, reservas : list) -> None:
        self.__nome = nome
        self.__estante = estante
        self.__reservas = reservas

#   GETTERS & SETTERS   #
    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def estante(self) -> list:
        return self.__estante
    
    @property
    def reservas(self) -> list:
        return self.__reservas
    
    @nome.setter
    def nome(self, novoNome : str) -> None:
        self.__nome = novoNome
    
    @estante.setter
    def estante(self, novaEstante : list) -> None:
        self.__estante = novaEstante

    @reservas.setter
    def reservas(self, novaReserva : list) -> None:
        self.__reservas = novaReserva
#   -----------------   #


#   Referente a locação de um livro pelo user
    def emprestimo(self, livro : Livro, quantidade : int = 1) -> None:
        def __revisao(__qtd : int) -> int: #    Função privada que printa a disponibilidade
            __exemplar = f'{__qtd} exemplares de {quantidade}' if __qtd > 1 else f'{__qtd} exemplar de {quantidade}'
            __o = 'os exemplares disponíveis' if __qtd > 1 else 'o exemplar disponível'

            print(f'\nSó será possível o emprestimo de: {__exemplar}. O que desejas fazer?')
            escolha = int(input(f'\n1. Locar {__o} e reservar o restante.\n2. Locar só {__o}\n3. Voltar ao menu \n-> '))
            return escolha
        
        def __locar(__qtdAdd):
            for i in self.__estante:
                if i[1] == livro:
                    __qtdAtual = i[0]
                    estante = self.__estante
                    estante.remove(i) 
                    estante.append([(__qtdAdd + __qtdAtual), livro])
                    self.__estante = estante
                    return
            self.__estante.append([__qtdAdd, livro]) # O livro e a quantidade é adicionada à estante do usuário.

        if quantidade > livro.qtdTotal: #   Caso o user escolha uma quantidade de livros que exceda o total guardado pelo acervo
            print('\nNão possuí essa quantidade de exemplares no acervo.')
            input('\n\nEnter para continuar...')
            return False
        
        if  quantidade > livro.qtdDisponivel: #    Caso o user escolha uma quantidade que exceda o disponível pelo acervo
            qtdSobra = quantidade - livro.qtdDisponivel

            revisao = __revisao(qtdSobra) #    Os return em True avisa o código lá na frente que houve uma locação, os return False indica o contrário
            match revisao:
                case 1: #   Caso ele queira locar todo estoque disponível e reservar os que já estão locados
                    __locar(livro.qtdDisponivel)
                    reserva = qtdSobra
                    return reserva
                case 2: #   Caso ele queire apenas locar todo estoque disponível
                    __locar(livro.qtdDisponivel)
                    return True
                case 3: #   Caso ele desista 
                    return False

        __locar(quantidade) #   Essa linha de código só é interpretada quando o user não é burro e escolhe uma quantidade normal
        return True

#   Referente a devolução de um livro
    def devolverLivro(self, livro : Livro, quantidadeDevolver : int = 1) -> list:
        
        def __devolver(qtd : int, lvr : Livro) -> list: #   Está função cria uma lista com o livro que deve ser devolvido e retorna a lista.
            __livroDevolver = [qtd, lvr]
            return __livroDevolver  

        
        for i in self.__estante: #   Esse bloco percorre a lista a procura do livro, caso ele não exista ou o usuário não tenha a quantidade solicitada, ele irá printar. Caso possua, ele vai retirar da estante o solicitado e mandar para o acervo.
            if i[0] >= quantidadeDevolver and i[1] == livro:
                
                if quantidadeDevolver - i[0] != 0: #    Caso tenha mais exemplares, ele apenas retira o solicitado da estante do usuário.
                    i[0] = quantidadeDevolver - i[0]
                    return __devolver(quantidadeDevolver, livro)
                
                
                else: #    Caso contrário, ele apaga da estante.
                    self.__estante.remove(i)
                    return __devolver(quantidadeDevolver, livro)
        print(f'O usuário não possuí em sua estante o livro ou a quatidade solicitada. Tente novamente mais tarde.')

#   Referente as informações da estante (livros locados e reservados)
    def imprimeEstante(self):
        def __print(objList : list, txt : str, txts : str): 
            __n = 1
            for i in objList:
                exemplar = f'exemplares {txts}' if i[0] > 1 else f'exemplar {txt}'
                print(f'| {__n}\t |\t {i[1].titulo} \t| {i[0]} {exemplar}. |', end='\n\n')
                __n += 1
        
        if self.__estante == [] and self.__reservas == []: 
            print('\nEstante vázia!')

        __print(self.__estante, 'locados', 'locado')
        __print(self.__reservas, 'reservados', 'reservado')
