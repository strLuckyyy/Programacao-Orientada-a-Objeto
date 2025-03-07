'''
Na função main:
• Crie nove objetos do tipo Pais que estejam situados em três continentes diferentes.
• Crie os três objetos do tipo Continente.
• Adicione os países aos respectivos continentes.
• Chame os métodos que apresentam as informações dos países e dos continentes.
'''
from pais import Pais
from continente import Continente



def main():
    brasil = Pais('BRA', 'Brasíl', 215.3, 8.56)
    argentina = Pais('ARG', 'Argentina', 47.3, 2.78)
    uruguai = Pais('URY', 'Uruguai', 3.444, 0.176)
    portugal = Pais('PRT', 'Portugal', 10.41, 0.092)
    espanha = Pais('ESP', 'Espanha', 47.45, 0.5)
    franca = Pais('FRA', 'França', 67.348, 0.543)
    china = Pais('CHN', 'China', 1409.67, 9.596)
    japao = Pais('JPN', 'Japão', 124.631, 0.377)
    coreia = Pais('KOR', 'Coreia do Sul', 51.446, 0.100)

    america = Continente('América do Sul')
    asia = Continente('Ásia')
    europa = Continente('Europa')

    america.addCountry(brasil)
    america.addCountry(argentina)
    america.addCountry(uruguai)

    teste = america.maxPopinCountry()
    print(teste)

if __name__ == '__main__':
    main()
