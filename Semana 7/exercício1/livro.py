class Livro: 
    def __init__(self, titulo : str, quantidadeTotal : int, quantidadeDisponivel : int) -> None:
        self.__titulo = titulo
        self.__qtdTotal = quantidadeTotal
        self.__qtdDisponivel = quantidadeDisponivel
    
#   GETTERS & SETTERS   #
    @property
    def titulo(self) -> str:
        return self.__titulo
    
    @property
    def qtdTotal(self) -> int:
        return self.__qtdTotal
    
    @property
    def qtdDisponivel(self) -> int:
        return self.__qtdDisponivel
    
    @titulo.setter
    def titulo(self, novoTitulo : str) -> None:
        self.__titulo = novoTitulo

    @qtdTotal.setter
    def qtdTotal(self, novaQtdTotal : int) -> None:
        self.__qtdTotal = novaQtdTotal

    @qtdDisponivel.setter
    def qtdDisponivel(self, novaQtdDisponivel : int) -> None:
        self.__qtdDisponivel = novaQtdDisponivel
#   -----------------   #


#   Referente a consulta da disponibilidade do livro
    def consultarDisponibilidade(self) -> bool:
        qtd = self.__qtdDisponivel
        exemplar = 'exemplares' if qtd > 1 else 'exemplar'
        disponivel = 'disponíveis' if qtd > 1 else 'disponível'
        
        if self.__qtdDisponivel != 0: 
            print(f'O livro {self.__titulo} está disponível com {self.__qtdDisponivel} {exemplar} {disponivel}.')
            return True

        print(f'O livro {self.__titulo} não está disponível para locação.')
        return False
