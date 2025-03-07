'''
Classe Continente:
◦ Um continente possui um nome e é composto por um conjunto de países.
◦ Crie um construtor que inicialize o nome do continente.
◦ Crie um método que permita adicionar países aos continentes.
◦ Crie um método que retorne a dimensão total do continente.
◦ Crie um método que retorne a população total do continente.
◦ Crie um método que retorne a densidade populacional do continente.
◦ Crie um método que retorne o país com maior população no continente.
◦ Crie um método que retorne o país com menor população no continente.
◦ Crie um método que retorne o país de maior dimensão territorial no continente.
◦ Crie um método que retorne o país de menor dimensão territorial no continente.
◦ Crie um método que retorne a razão territorial do maior país em relação ao menor país.
'''
from __future__ import annotations
from pais import Pais



class Continente:
    def __init__(self, nome: str) -> None:
        self.__name = nome
        self.__countries: list[Continente] = []


    @property
    def nome(self) -> str:
        return self.__name
    

    @property
    def country(self) -> list[Pais]:
        return self.__countries
  
    
    #Crie um método que permita adicionar países aos continentes.
    def addCountry(self, pais: Pais):
        self.__countries.append(pais)


    #Crie um método que retorne a dimensão total do continente.
    def totalDimension(self) -> float:
        return sum(pais.dimensao for pais in self.__countries)


    #Crie um método que retorne a população total do continente.
    def totalPop(self) -> float:
        return sum(pais.populacao for pais in self.__countries)


    #Crie um método que retorne a densidade populacional do continente.
    def popDensity(self) -> float:
        return sum(pais.popuDensity() for pais in self.__countries)


    #Crie um método que retorne o país com maior população no continente.
    def maxPopinCountry(self) -> Pais:
        maxPop = self.__countries[0]   
        
        for pais in self.__countries:
            if pais.populacao > maxPop.populacao: maxPop = pais

        return maxPop


    def minPopinCountry(self):
        pass


    def ratioTerritoryCountryvsCountry(self) -> float:
        pass

    
    def imprimi_info(self):
        pass
