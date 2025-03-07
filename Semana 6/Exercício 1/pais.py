'''
Classe Pais:
◦ Classe que representa um país.
◦ Um país possui um código ISO 3166-1 (ex.: BRA), um nome (ex.: Brasil), uma população (ex.: 193.946.886) e uma dimensão em Km2 
(ex.: 8.515.767,049). Além disso, um país mantém uma lista de outros países com os quais ele faz fronteira.
◦ Crie um construtor que inicialize o código ISO, o nome e a dimensão do país.
◦ Crie os métodos de acesso e modificadores (getter/setter) para os atributos código ISO, nome, população e dimensão.
◦ Crie um método que permita verificar se dois objetos representam o mesmo país (igualdade semântica). 
Dois países são iguais se tiverem o mesmo código ISO.
◦ Crie um método que informe se outro país é limítrofe do país que recebeu a mensagem.
◦ Crie um método que retorne a densidade populacional do país.
◦ Crie um método que receba um país como parâmetro e retorne a lista de vizinhos comuns aos dois países. 
Considere que um país tem no máximo 40 outros países com os quais ele faz fronteira.
'''
from __future__ import annotations



class Pais:
    def __init__(self, ISO: str, nome: str, populacao_Mi: float, dimensao_Mi_KM2: float) -> None:
        self.__name = nome
        self.__ISO = ISO
        self.__population = populacao_Mi
        self.__dimension = dimensao_Mi_KM2
        self.__neigh: list[Pais] = []

    @property
    def nome(self):
        return self.__name
    
    @property
    def iso(self):
        return self.__ISO
    
    @property
    def populacao(self):
        return self.__population
    
    @property
    def dimensao(self):
        return self.__dimension
    
    @nome.setter
    def nome(self, nome):
        self.__name = nome
    
    @iso.setter
    def iso(self, iso):
        self.__ISO = iso
    
    @populacao.setter
    def populacao (self, pop):
        self.__population = pop

    @dimensao.setter
    def dimensao(self, dimension):
        self.__dimension = dimension


    #Crie um método que permita verificar se dois objetos representam o mesmo país (igualdade semântica). 
    #Dois países são iguais se tiverem o mesmo código ISO.
    def __eq__(self, pais: Pais) -> bool:
        if id(self) == id(pais): return True
        elif self.ISO == pais.ISO: return True
        else: return False


    def addNeigh(self, pais: Pais) -> None:
        self.__neigh.append(pais)


    #Crie um método que informe se outro país é limítrofe do país que recebeu a mensagem.
    def isNeigh(self, pais: Pais) -> bool:
        for i in self.__neigh:
            if self.__neigh[i] == pais: return True
        return False

    
    #Crie um método que retorne a densidade populacional do país.
    def popuDensity(self) -> float:
        popDensity = self.__population / self.__dimension
        return popDensity


    #Crie um método que receba um país como parâmetro e retorne a lista de vizinhos comuns aos dois países.
    def neighinCommun(self, pais: Pais) -> list[Pais]:
        communNeigh: list = []
        for country1 in self.__neigh:
            for country2 in pais.__neigh:
                if country1 == country2: communNeigh.append(country1); break
        return communNeigh
