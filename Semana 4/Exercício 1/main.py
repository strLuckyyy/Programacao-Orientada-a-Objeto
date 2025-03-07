'''
Na função main:
• Crie um objeto do tipo FuncionarioCaixa, chamado funcionario. Tudo que
for necessário para criar este objeto, deve ser solicitado para o usuário.
• Imprima o resultado das operações: 2+2, 5-4, 2x3, 6/3, 7+2, 8x3. As operações
devem ser feitas através da calculadora do objeto funcionário criado.
• Neste método, crie um objeto do tipo Empresa chamado empresa1, com nome
solicitado para o usuário, com o funcionário criado anteriormente e um novo
funcionário que deve ser criado. Tudo que for necessário para criar esta empresa
(que já não tenha sido criado) deve ser solicitado para o usuário.
• Imprima as informações desta empresa.
'''
from calculadora import Calculadora
from empresa import Empresa
from funcionario import FuncionarioCaixa
from ficha import Ficha



def main():
    calc1 = Calculadora(input('Qual a cor da calculadora do 1o funcionário? '), int(input('Qual a memória da calculadora do funcionário? ')))
    print('\n')

    Funcionario_1 = FuncionarioCaixa(input('Qual o nome do funcionário? '), input('Qual o endereço do funcionário? '), calc1)

    nome: list = ['2 + 2', '5 - 4', '2 * 3', '6 / 3', '7 + 2', '8 * 3']
    valor: list = []

    valor.append(Funcionario_1.soma(2.0, 2.0))
    valor.append(Funcionario_1.subtracao(5.0, 4.0))
    valor.append(Funcionario_1.multip(2.0, 3.0))
    valor.append(Funcionario_1.divisao(6.0, 3.0))
    valor.append(Funcionario_1.soma(7.0, 2.0))
    valor.append(Funcionario_1.multip(8.0, 3.0))
    print('\n')

    info_contas = Ficha(f'RESULTADO DA CALCULADORA DO {Funcionario_1.nameUpper()}')
    info_contas.titulo()
    info_contas.conteudo(nome, valor)
    print('\n')

    calc2 = Calculadora(input('Qual a cor da calculadora do 2o funcionário? '), int(input('Qual a memória da calculadora do funcionário? ')))
    print('\n')

    Funcionario_2 = FuncionarioCaixa(input('Qual o nome do funcionário? '), input('Qual o endereço do funcionário? '), calc2)
    print('\n')

    empresa1 = Empresa(input('Qual o nome da Empresa? '), Funcionario_1, Funcionario_2)
    print('\n')

    empresa1.imprimi_info()


if __name__ == '__main__':
    main()
