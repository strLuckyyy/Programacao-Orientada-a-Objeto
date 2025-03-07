class Lampada:
    def __init__(self, potencia: int, cor: str, tecno: str, ligada: bool = False) -> None:
        self.potencia = potencia
        self.ligada = ligada
        self.cor = cor
        self.tecnologia = tecno
    

    def alterEstado(self, ligada: bool):
        self.ligada = ligada

def main():
    lamp1 = Lampada(9, 'verde', 'Led', False)
    lamp2 = Lampada(50, 'branca', 'Incandecente', False)

    lamp1.alterEstado(True)

    print(f'Lâmpada 1: \n'
          f'\tPotência = {lamp1.potencia}W\n'
          f'\tEstado = {lamp1.ligada}\n'
          f'\tCor = {lamp1.cor}\n'
          f'\tTecnologia = {lamp1.tecnologia}')


    print(f'\nLâmpada 2: \n'
          f'\tPotência = {lamp2.potencia}W\n'
          f'\tEstado = {lamp2.ligada}\n'
          f'\tCor = {lamp2.cor}\n'
          f'\tTecnologia = {lamp2.tecnologia}\n')


if __name__ == '__main__':
    main()