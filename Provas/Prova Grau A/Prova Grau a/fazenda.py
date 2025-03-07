from animal import Animal



class Fazenda:
    def __init__(self) -> None:
        self.__animais: list[Animal] = []
    

    @property
    def animais(self):
        return self.__animais
    

    @animais.setter
    def animais(self, animais):
        self.__animais = animais


    def adicionar_animal(self, animal: Animal):
        self.__animais.append(animal)


    def calcular_valor_animais(self):
        valor: float = 0.0
        lista = self.__animais

        for i in range(len(lista)):
            lista[i].calcula_preco_animal()
            c_juros = lista[i].calcula_juros()

            valor += lista[i].calcula_valor_de_venda(c_juros)
        
        return valor


    def idade_media(self) -> float:
        media: float = 0.0
        lista = self.__animais
        
        c = 0
        for i in range(len(lista)):
            media += lista[i].idade
            c += 1

        media /= c
        return media


    def aumenta_idade(self, nome: str):
        nome = nome.lower()
        
        for animal in self.__animais:
            animal_fazenda = animal.nome.lower()

            if nome == animal_fazenda:
                animal.aumenta_idade()
                return True
        return False    


    def imprimi_info(self):
        print('-' * 50)
        print('FAZENDA DO GALO CEGO')
        print('-' * 50)

        for animais in self.animais:
            animais.imprimi_info()
        
