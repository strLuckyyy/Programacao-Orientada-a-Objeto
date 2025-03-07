from pais import Pais


class Continente:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__paises: list[Pais] = []

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def paises(self) -> list[Pais]:
        return self.__paises

    def adiciona_pais(self, pais: Pais) -> None:
        self.paises.append(pais)

    def dimensao_continente(self) -> float:
        return sum(pais.dimensao for pais in self.paises)

    def dp_continente(self) -> float:
        return sum(pais.densidade_populacional() for pais in self.paises)

    def maior_populacao(self) -> Pais:
        maior = self.paises[0]
        for pais in self.paises:
            if pais.populacao > maior.populacao:
                maior = pais
        return maior

    def menor_populacao(self) -> Pais:
        menor = self.paises[0]
        for pais in self.paises:
            if pais.populacao < menor.populacao:
                menor = pais
        return menor

    def maior_dimensao(self) -> Pais:
        maior = self.paises[0]
        for pais in self.paises:
            if pais.dimensao > maior.dimensao:
                maior = pais
        return maior

    def menor_dimensao(self) -> Pais:
        menor = self.paises[0]
        for pais in self.paises:
            if pais.dimensao < menor.dimensao:
                menor = pais
        return menor

    def razao_territorial(self) -> float:
        return self.maior_dimensao().dimensao / self.menor_dimensao().dimensao
