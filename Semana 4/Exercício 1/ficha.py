class Ficha:
    def __init__(self, txt: str) -> None:
        self.__texto = txt
        
    
    @property
    def txt(self):
        return self.__texto
    

    @txt.setter
    def txt(self, txt):
        self.__texto = txt

    
    def titulo(self):
        print('-' * 50)
        print(f'{self.txt}'.center(50))
        print('-' * 50)
    

    def conteudo(self, nome: list, valor: list):
        for i in range(len(nome)):
            print(f'{nome[i]}: {valor[i]}'.center(50))
        print('=' * 50)
