'''
Crie uma classe para calcular o imposto de renda simplificado chamada
IRSimplificado. A classe IRSimplificado possui o nome do contribuinte, o ano de
nascimento, a profissão, a escolaridade, a renda mensal e o número de
dependentes do contribuinte. Crie os seguintes métodos: 
• método que calcula e retorna a idade do contribuinte
• método que calcula e retorna a renda anual do contribuinte
• método que calcula e retorna a renda per capita mensal
• método que retorna a alíquota de IR máxima
• método que retorna o valor da dedução do IR segundo a alíquota de IR máxima
• método que calcula e retorna o valor do imposto de renda mensal
• método que calcula e retorna o valor do imposto de renda anual
Respeitar as faixas para as alíquotas segundo a tabela abaixo.
Escreva um programa que instancie um objeto de forma dinâmica e solicite que o
usuário informe todos os atributos. Em seguida, faça o cálculo do imposto de renda
e imprima todos os dados.
'''

import os

class IRSimplificado:
    def __init__(self, nome_contribuinte: str, ano_nascimento: int, profissao: str, escolaridade: str, renda_mensal: float, numero_dependentes: int) -> None:
        self.nome = nome_contribuinte
        self.nascimento = ano_nascimento
        self.profissao = profissao
        self.escolaridade = escolaridade
        self.renda_m = renda_mensal
        self.n_dependentes = numero_dependentes

    
    def calcIdade(self, nascimento, ano_atual):
        idade = ano_atual - nascimento
        return idade


    def calcRendaAnual(self, renda_mensal):
        renda_anual = renda_mensal * 12
        return renda_anual


    def calcRendaPerCapitaMensal(self, renda_mensal, n_dependentes):
        renda_per_capita = renda_mensal / (n_dependentes + 1)
        return renda_per_capita


    def returnAliquota(self, renda_mensal):
        aliquota = 0

        if 2826.65 > renda_mensal >= 2259.21:
            aliquota = 7.5
            return aliquota
        if 3751.05 > renda_mensal >= 2826.66:
            aliquota = 15
            return aliquota
        if 4664.68 > renda_mensal >= 3751.06:
            aliquota = 22.5
            return aliquota
        if renda_mensal >= 4664.68:
            aliquota = 27.5
            return aliquota
        
        return aliquota


    def deducaoIR(self, aliquota):
        deducao = 0

        if aliquota == 7.5:
            deducao = 169.44
            return deducao
        if aliquota == 15:
            deducao = 381.44
            return deducao
        if aliquota == 22.5:
            deducao = 662.77
            return deducao
        if aliquota == 27.5:
            deducao = 896.00
            return deducao
        
        return deducao


    def calcImpostoMensal(self, renda_mensal, aliquota, deducao):
        IM = 0
        if aliquota > 0:
            IM = renda_mensal - (renda_mensal - deducao * (aliquota / 100))
            return IM
        return IM


    def calcImpostoAnual(self, renda_anual, aliquota, deducao):
        IA = 0
        if aliquota > 0:
            IA = renda_anual - (renda_anual - (deducao * (aliquota / 100) * 12))
            return IA
        return IA


    def imprime_dados(self, user):

        nome = user.nome
        nascimento = user.nascimento
        dependentes = user.n_dependentes
        profissao = user.profissao
        escolaridade = user.escolaridade
        renda_mensal = user.renda_m
        renda_anual = user.calcRendaAnual(renda_mensal)
        aliquota = user.returnAliquota(renda_mensal)
        deducao = user.deducaoIR(aliquota)

        print(
            '-' * 50, '\n',
            'Dados'.center(50), '\n',
            '-' * 50, '\n',
            f'Nome\t\t\t|\t{nome}\n',
            f'Idade\t\t\t|\t{user.calcIdade(nascimento, 2024)}\n',
            f'Número de Dependentes\t|\t{dependentes}\n',
            f'Profissão\t\t|\t{profissao}\n',
            f'Escolaridade\t\t|\t{escolaridade}\n',
            '-' * 50, '\n',
            f'Renda Mensal\t\t|\t{renda_mensal}\n',
            f'Renda Anual\t\t|\t{renda_anual}\n',
            f'Renda Per Capita\t|\t{user.calcRendaPerCapitaMensal(renda_mensal, dependentes)}\n',
            '-' * 50, '\n',
            f'Alíquota\t\t|\t{aliquota}\n',
            f'Dedução IR\t\t|\t{deducao}\n',
            '-' * 50, '\n',
            f'Imposto Mensal\t\t|\t{user.calcImpostoMensal(renda_mensal, aliquota, deducao)}\n',
            f'Imposto Anual\t\t|\t{user.calcImpostoAnual(renda_anual, aliquota, deducao)}\n',
            '-' * 50, '\n'
        )


def cadastro():
    i = []
    
    i.append(input('Qual o nome do cliente? '))
    i.append(int(input('Qual o ano que o cliente nasceu? ')))
    i.append(input('Qual a profissão do cliente? '))
    i.append(input('Qual a escolaridade do cliente? '))
    i.append(float(input('Qual a renda mensal do cliente? ')))
    i.append(int(input('Quantos dependentes o cliente possuí? ')))

    return i


def main():
    os.system('cls')

    i1 = cadastro()
    user = IRSimplificado(i1[0], i1[1], i1[2], i1[3], i1[4], i1[5])
    user.imprime_dados(user)


if __name__ == '__main__':
    main()
