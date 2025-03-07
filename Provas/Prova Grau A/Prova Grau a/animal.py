class Animal:
    def __init__(self, nome: str, tipo: str, peso: float, idade: int) -> None:
        self.__nome = nome
        self.__tipo = tipo
        self.__peso = peso
        self.__idade = idade
        self.__preco: float = 0.0


    @property
    def nome(self):
        return self.__nome
    

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    @property
    def tipo(self):
        return self.__tipo
    

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
    

    @property
    def peso(self):
        return self.__peso
    

    @peso.setter
    def peso(self, peso):
        self.__peso = peso
    

    @property
    def idade(self):
        return self.__idade
    
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade


    def aumenta_idade(self):
        self.__idade = self.__idade + 1
    

    def calcula_preco_animal(self):
        idade = self.__idade
        peso = self.__peso

        if idade <= 10: 
            self.__preco = peso / 3
            return self.__preco

        elif idade >= 11 and idade <= 20: 
            self.__preco = peso / 2 
            return self.__preco

        elif idade >= 21 and idade <= 30:
            self.__preco = peso + (100 / (peso * 20))
            return self.__preco

        elif idade > 30: 
            self.__preco = peso + (100 / (peso * 73))
            return self.__preco


    def calcula_juros(self):
        juros: float = 0.0
        preco = self.__preco

        if preco >= 1.0 and preco <= 100.0:
            juros = 0.10
            return juros
        
        if preco >= 101.0 and preco <= 249.0:
            juros = 0.29
            return juros
        
        if preco >= 250.0 and preco <= 986.0:
            juros = 0.61
            return juros
        
        if preco >= 987.0:
            juros = 0.75
            return juros


    def calcula_valor_de_venda(self, juros):
        valor_venda = 0.0

        valor_venda = self.__preco * juros
        return valor_venda


    def imprimi_info(self):
        print('-' * 50)
        print('Nome:', f'\t{self.__nome}')
        print('Tipo:', f'\t{self.__tipo}')
        print('Peso:', f'\t{self.__peso}')
        print('Idade:', f'\t{self.__idade}')
        print('Preço:', f'\t{self.__preco:.2f}')
