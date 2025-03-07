from acervo import Acervo
from livro import Livro
from usuario import Usuario
import os

def wait() -> None:
    input('\nEnter para continuar...')
    os.system('cls')

def menu() -> int:
    print('BIBLIOTECA'.center(50))
    print(
        '\n1. Minha Estante',
        '\n2. Consultar Acervo',
        '\n3. Solicitar Emprestimo',
        '\n4. Devolver Livro',
        '\n5. Adicionar Livros ao Acervo',
        '\n6. Remover Livros do Acervo',
        '\n7. Relatório Local'
        '\n0. Sair'
    )
    escolha = int(input('Qual opção você deseja acessar?\n -> '))
    return escolha

def main() -> None:
    os.system('cls')

    livros = [Livro('Pedalinho', 10, 10), Livro('Principe', 5, 5), Livro('País dos Horrores', 9, 9), Livro('A volta', 2, 2), Livro('Sambinha', 1, 1)]
    user = Usuario(input('Usuário: '), [], [])
    biblioteca = Acervo(livros)
    
    loop = True
    while loop:
        opcao = menu()
        while loop:
            match opcao:
                case 1:
                    user.imprimeEstante()
                    wait()
                    break

                case 2:
                    biblioteca.consultarAcervo()
                    wait()
                    break

                case 3:
                    biblioteca.solicitarEmprestimo(user)
                    wait()
                    break

                case 4:
                    if user.estante != []:
                        biblioteca.devolverLivros(user, input('Qual livro desejas devolver? '), input('Quantos exemplares desejas devolver? '))
                    else: 
                        print('\nVocê não possuí livros pendêntes.')
                    wait()
                    break

                case 5:
                    nome = input('Qual o nome do livro? ')
                    qtd = input('Quantos desejas adicionar? ')
                    biblioteca.adicionarLivros(Livro(nome, qtd, qtd))
                    wait()
                    break

                case 6:
                    biblioteca.removerLivro()
                    wait()
                    break

                case 7:
                    biblioteca.relatorio(user)
                    wait()
                    break

                case 0:
                    os.system('cls')
                    print('Obrigado por usar meu programa!')
                    return


if __name__ == "__main__":
    main()
