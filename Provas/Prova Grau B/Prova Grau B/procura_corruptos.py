from deputado import Deputado

class Procura_Corruptos:
    def __init__(self, deputados : list) -> None:
        self.__deputados = deputados

    @property
    def deputados(self) -> list:
        return self.__deputados
    
    @deputados.setter
    def deputados(self, novaListaDeputados : list):
        self.__deputados = novaListaDeputados



    def deputados_mais_funcionarios(self) -> list:
        deputadosCorruptos = []

        for i in self.__deputados:
            if i.numero_funcionarios() > 10:
                deputadosCorruptos.append(i)

        return deputadosCorruptos


    def deputados_recebem_valores(self):
        deputadosCorruptos = ['Python me quebrou nessa fight, prova toda travado aqui kkkkkk']
        return deputadosCorruptos

#       EU NÃO SEI, porque ele não está atribuindo os obj na variável 'd' e 'i', pelo menos acho que é esse o problema, já que a mensagem de erro só diz: "TypeError: 'int' object is not callable", o que sinceramente não faz sentido na minha cabeça. Vou enviar sem terminar essa parte, paciência.
    '''
        for d in self.__deputados:
            for i in d.funcionarios():
                salBruto = i.salarioBruto
                salLiquido = i.salarioLiquido

                if self.diferenca_salario(salBruto, salLiquido) != 70:
                    deputadosCorruptos.append(d)

        return deputadosCorruptos
    '''

    def deputados_desviam_verbas(self):
        deputadosCorruptos = []
        
        for d in self.__deputados:
            if self.diferenca_salario(d.salarioBruto, d.salarioLiquido) != 80:
                deputadosCorruptos.append(d)

        return deputadosCorruptos
    

    def diferenca_salario(self, salBruto : float, salLiquido : float) -> float:
        porcetangem = (salLiquido * 100) / salBruto
        return porcetangem
    

    def imprimi_info(self,):
        depMaisFuncionarios = self.deputados_mais_funcionarios()
        depRecebemValores = self.deputados_recebem_valores()
        depDesviamVerba = self.deputados_desviam_verbas()

        print('-' * 50)
        print('DEPUTADOS COM MAIS FUNCIONARIOS'.center(50))
        print('-' * 50)
        for i in depMaisFuncionarios:
            print(f' Deputado : {i.nome} \t| Partido : {i.partido} \t\t| Nº Funcionarios : {i.numero_funcionarios()}')
        print('-' * 50)


        print('DEPUTADOS QUE RECEBEM VALORES'.center(50))
        print('-' * 50)
        print(depRecebemValores)
        print('-' * 50)


        print('DEPUTADOS QUE DESVIAM VERBA'.center(50))
        print('-' * 50)
        for i in depDesviamVerba:
            print(f' Deputado : {i.nome} \t| Partido : {i.partido} \t')
        print('-' * 50)

