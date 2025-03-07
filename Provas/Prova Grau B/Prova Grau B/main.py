from funcionario import Funcionario
from deputado import Deputado
from federal import Federal
from estadual import Estadual
from procura_corruptos import Procura_Corruptos
import random
import os



#   Função que aleatoriza os funcionarios
def randomizando_funcionarios(numeroFuncionarios) -> list[Funcionario]:
    nomes = ['Janet', 'Joao', 'Alexa', 'Daniel', 'Sara', 'Dolores', 'Pedro', 'Aqueleali', 'Laura', 'Caroline', 'Livia', 'Fabricio', 'Fabio', 'Lucas', 'Fulano', 'Ciclano', 'Beltrano', 'Furacao', 'George', 'Marima', 'Aquele outro ali']
    index = random.randint(0, 20)
    nomes = nomes[index]
    lista = []

    i = 0
    while i < numeroFuncionarios:
        lista.append(Funcionario(nomes, randomizando(), randomizando()))
        i += 1
    
    return lista



def randomizando() -> float:
    return (random.random() * 1000)


def main():
    funcionariosDep1 = randomizando_funcionarios(12)
    funcionariosDep2 = randomizando_funcionarios(34)
    funcionariosDep3 = randomizando_funcionarios(3)
    funcionariosDep4 = randomizando_funcionarios(34)
    funcionariosDep5 = randomizando_funcionarios(21)
    funcionariosDep6 = randomizando_funcionarios(10)
    funcionariosDep7 = randomizando_funcionarios(10)
    funcionariosDep8 = randomizando_funcionarios(4)
    funcionariosDep9 = randomizando_funcionarios(9)
    funcionariosDep10 = randomizando_funcionarios(32)

    deputados = [
        Estadual('Dep 1', int(randomizando()), 20.000, 22.000, len(funcionariosDep1), 'RS'),
        Federal('Dep 2', int(randomizando()), 25.000, 32.000, len(funcionariosDep2), 123),
        Federal('Dep 3', int(randomizando()), 10.000, 8.000, len(funcionariosDep3), 456),
        Federal('Dep 4', int(randomizando()), 13.000, 13.000, len(funcionariosDep4), 789),
        Federal('Dep 5', int(randomizando()), 9.000, 7.200, len(funcionariosDep5), 'RS'),
        Federal('Dep 6', int(randomizando()), 22.000, 17.600, len(funcionariosDep6), 'SP'),
        Federal('Dep 7', int(randomizando()), 32.000, 30.000, len(funcionariosDep7), 321),
        Federal('Dep 8', int(randomizando()), 25.000, 29.000, len(funcionariosDep8), 654),
        Federal('Dep 9', int(randomizando()), 10.000, 8.000, len(funcionariosDep9), 'SC'),
        Federal('Dep 10', int(randomizando()), 21.000, 16.800, len(funcionariosDep10), 'RJ')
                 ]
    
    corruptos = Procura_Corruptos(deputados)

    corruptos.imprimi_info()


if __name__ == '__main__':
    os.system('cls')
    main()