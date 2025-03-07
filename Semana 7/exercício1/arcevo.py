class Acervo: 
    def __init__(self, livros: list) -> None:
        self.__livros = livros

    @property
    def livros(self):
        return self.__livros

    
    def consultar_acervo(self):
        for i in self.livros:
            print(f'{i + 1} | {self.livros}')
            print()

    
    def solicitar_emprestimo(self):
        id = input('Qual o número do livro que você deseja acessar? ')
        confi = input(f'Confirma a escolha do livro {self.livros[id].titulo}? (s/n)')

        if confi == 's':
            self.livros[id].verificar_dispo()
        
    
    def solicitar_reserva(self):
        pass


    def adicionar_livros(self):
        pass


    def devolver_livros(self):
        pass


    def acervo_info(self):
        pass
