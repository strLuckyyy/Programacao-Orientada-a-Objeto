from __future__ import annotations


class Pais:
    def __init__(self, iso: str, nome: str, dimensao: float):
        self.__iso = iso
        self.__nome = nome
        self.__populacao = 0
        self.__dimensao = dimensao
        self.__fronteira: list[Pais] = []

    @property
    def iso(self) -> str:
        return self.__iso

    @iso.setter
    def iso(self, iso: str) -> None:
        self.__iso = iso

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def populacao(self) -> int:
        return self.__populacao

    @populacao.setter
    def populacao(self, populacao: int) -> None:
        self.__populacao = populacao

    @property
    def dimensao(self) -> float:
        return self.__dimensao

    @dimensao.setter
    def dimensao(self, dimensao: float) -> None:
        self.__dimensao = dimensao

    @property
    def fronteira(self) -> list[Pais]:
        return self.__fronteira

    def __eq__(self, pais: Pais) -> bool:
        if id(self) == id(pais):
            return True
        elif self.iso == pais.iso:
            return True
        else:
            return False

    def adiciona_fronteira(self, pais: Pais) -> None:
        self.__fronteira.append(pais)

    def verifica_fronteira(self, pais: Pais) -> None:
        limitrofe = True
        for p in self.__fronteira:
            if p == pais:
                print(f"{pais.nome} é limítrofe de {self.nome}")
                break
        if not limitrofe:
            print(f"{pais.nome} não é limítrofe de {self.nome}")

    def densidade_populacional(self) -> float:
        return self.populacao / self.dimensao

    def paises_vizinhos(self, pais: Pais) -> list[Pais]:
        vizinhos = []
        for p1 in self.fronteira:
            for p2 in pais.fronteira:
                if p1 == p2:
                    vizinhos.append(p2)
                    break
        return vizinhos
