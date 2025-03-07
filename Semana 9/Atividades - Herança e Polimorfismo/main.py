from veiculo import Veiculo
from terrestre import Terrestre
from aquatico import Aquatico
from aereo import Aereo
import os

def main():
    os.system('cls')
    fusquinha = Terrestre(1990, 200, 100, 'Fusca Top', 4, 2)
    fusquinha.info()


if __name__ == '__main__':
    main()