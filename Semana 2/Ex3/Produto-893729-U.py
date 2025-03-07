class Produto:
    def __init__(self, nome: str, valor: float, descricao: str, qntEstoque: int) -> None:
        self.nome = nome
        self.valor = valor
        self.desc = descricao
        self.qntEstoque = qntEstoque

    
def main():
    BalaFini = Produto('Bala Fini', 12.99, 'Bala doce estilo canudo', 3000)
    print(f'\tNome: {BalaFini.nome}\n'
          f'\tValor: {BalaFini.valor}\n'
          f'\tDescrição: {BalaFini.desc}\n'
          f'\tQuantidade de Estoque: {BalaFini.qntEstoque}')


if __name__ == '__main__':
    main()
