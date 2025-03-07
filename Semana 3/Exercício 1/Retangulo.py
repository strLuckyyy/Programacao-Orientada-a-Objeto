'''
Crie uma classe chamada Retângulo. Um retângulo possui uma base e uma altura.
Crie os métodos necessários para que o usuário possa obter informações sobre a
base, a altura e a área do retângulo.
'''

import os

class Retangulo:
    def __init__(self, base: float, altura: float) -> None:
        self.baseRetangulo = base
        self.alturaRetangulo = altura

    
    def areaCalculo(self, base: float, altura: float):
        area = base * altura
        return area


    def infoRetan(self, baseR, alturaR, areaR):
        print(f'Esse retangulo possuí:\n'
            f'\tBase = {baseR}\n'
            f'\tAltura = {alturaR}\n'
            f'\tArea = {areaR}\n')


def main():
    os.system('cls')

    base: float = float(input('Qual a base do Retângulo? '))
    altura: float = float(input('Qual a altura do Retângulo? '))

    Retangulo1 = Retangulo(base, altura)

    area = Retangulo1.areaCalculo(base, altura)

    Retangulo1.infoRetan(base, altura, area)


main()