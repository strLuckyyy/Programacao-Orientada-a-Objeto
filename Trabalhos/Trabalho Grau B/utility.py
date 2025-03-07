#   Trabalho do Grau B de Programação Orientada a Objetos de Abrahão Francis e Lucas Moraes.

import os
class Utility:

#   limpa a tela
    def clear(self):
        os.system('cls')

#   espera um input do usuário para prosseguir.
    def wait(self,frase):
        input(f'{frase}\n\nPressione Enter para continuar..\n')
        os.system('cls')

#   usado apenas para mostrar mais claramente a impressão de um método 'execute' de um processo
    def separacao(self) -> None:
        print('-' * 50)
