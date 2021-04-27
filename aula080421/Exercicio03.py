'''Ler dois valores inteiros e apresentar a diferença do maior pelo menor'''


def is_int(valor):
    try:
        int(valor)
    except:
        return False

    return True


if __name__ == '__main__':
    # ANTES
    # n1 = input()
    # while is_int(n1) == False:
    #     n1 = input()
    # n1 = int(n1)
    #
    # n2 = input()
    # while is_int(n2) == False:
    #     n2 = input()
    # n2 = int(n2)
    #
    # if n1 > n2:
    #     resultado = n1 - n2
    # else:
    #     resultado = n2 - n1
    #
    # print(resultado)

    # DEPOIS
    n1 = input('Digite o primeiro número: ')
    while is_int(n1) == False:
        print('Valor inválido!')
        n1 = input('Digite o primeiro número: ')
    n1 = int(n1)

    n2 = input('Digite o segundo número: ')
    while is_int(n2) == False:
        print('Valor inválido!')
        n2 = input('Digite o segundo número: ')
    n2 = int(n2)

    if n1 > n2:
        resultado = n1 - n2
        print(f'O resultado de {n1} - {n2} = {resultado}')
    else:
        resultado = n2 - n1
        print(f'O resultado de {n2} - {n1} = {resultado}')