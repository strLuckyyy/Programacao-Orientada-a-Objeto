class Produto:
    def __init__(self,codigo,nome,preco):
        self.__codigo = codigo
        self.__nome = nome
        self.__preco = preco

    def get_codigo(self):
        return self.__codigo
    
    def get_nome(self):
        return self.__nome
    
    def get_preco(self):
        return self.__preco
    
    def set_codigo(self,new):
        self.__codigo = new
    
    def set_nome(self,new):
        self.__nome = new
    
    def set_preco(self,new):
        self.__preco = new
    
    def imprime_infos(self):
        print(f'Nome do Produto: {(self.get_nome()).capitalize()}\nCódigo do Produto: {self.get_codigo()}\nPreço do Produto: R${float(self.get_preco())}')