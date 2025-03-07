from aluno import Aluno

def main():
    a1 = Aluno("Aristides", 34, 1234)
    a2 = Aluno("Aristotelina", 35, 1235)

    if a1 == a2:
        print("Mesmo aluno")
    else:
        print("Alunos diferentes")

    a1.imprime_info()
    a2.imprime_info()
    

if __name__ == '__main__':
    main()