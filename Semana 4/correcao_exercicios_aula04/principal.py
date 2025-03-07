from calculadora import Calculadora
from funcionario import FuncionarioCaixa
from empresa import Empresa


def main():
    calc1 = Calculadora("Lilás", 400)
    calc2 = Calculadora("Azul", 500)

    func1 = FuncionarioCaixa(input("Informe o nome do primeiro funcionário: "), input("Endereço do funcionário: "), calc1)
    func2 = FuncionarioCaixa(input("Informe o nome do segundo funcionário: "), input("Endereço do funcionário: "), calc2)

    empresa = Empresa(input("Informe o nome da empresa: "), func1, func2)
    empresa.imprime_info()

    print(f"\nOperações realizadas pelo funcionário: {func1.nome}")
    print(f"2 + 2: {func1.soma(2.0, 2.0)}")
    print(f"5 - 4: {func1.subtrai(5.0, 4.0)}")
    print(f"2 x 3: {func1.multiplica(2.0, 3.0)}")
    print(f"\nOperações realizadas pelo funcionário: {func2.nome}")
    print(f"6 / 3: {func2.divide(6.0, 3.0)}")
    print(f"7 + 2: {func2.soma(7.0, 2.0)}")
    print(f"8 x 3: {func2.multiplica(8.0, 3.0)}")


if __name__ == '__main__':
    main()
