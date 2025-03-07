class Quarto:
    def __init__(self,numero,categoria,diaria,consumo):
        self.__numero = numero
        self.__categoria = categoria
        self.__diaria = diaria
        self.__consumo = consumo

    def get_numero(self):
        return self.__numero
    
    def get_categoria_fim(self):
        return self.__categoria

    def get_categoria(self):
        if self.__categoria == 's':
            return 'Standard'
        elif self.__categoria == 'm':
            return 'Master'
        elif self.__categoria == 'p':
            return 'Premium'
    
    def get_diaria(self):
        return self.__diaria
    
    def get_consumo(self):
        return self.__consumo
    
    def limpa_consumo(self):
        self.set_consumo('Nada')

    def imprime_infos(self):
        print(f'Número do quarto: {self.get_numero()}\nCategoria do quarto: {self.get_categoria()}\nDiaria do quarto: {self.get_diaria()}\nConsumo do quarto: {self.get_consumo()}')

    def set_consumo(self,consumo):
        self.__consumo = consumo

    def adiciona_consumo(self,codigo):
        lista = self.get_consumo()
        if lista == 'Nada':
            lista = []
        lista.append(codigo)
        self.set_consumo(lista)
