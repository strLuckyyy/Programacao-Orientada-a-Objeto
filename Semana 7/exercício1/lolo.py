lista = [[1, 'lolo'], [2, 'lolo'], [3, 'lolo']]

def testes():
    
    loop = True
    while loop:
        co = int(input('lolo'))
        while loop:
            print('loop')
            match co:
                case 1:
                    print(2)
                case 2:
                    print(co)
                    break

novalista = testes()

print(lista, novalista)