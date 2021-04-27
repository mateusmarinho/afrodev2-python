'''Criar um algoritmo que recebe 2 números e multiplica o primeiro pelo segundo através
de somas repetidas (ex: 2 x 3 = 2 + 2 + 2)'''


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
    # if n2 == 0:
    #     res = 0
    # else:
    #     res = 0
    #     cont = 0
    #     while cont != n2:
    #         res += n1
    #         cont += 1
    #
    # print(res)

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

    res = 0
    cont = 0

    if n2 >= 0:
        while cont < n2:
            res += n1
            cont += 1
    else:
        while cont > n2:
            res -= n1
            cont -= 1

    print(f'{n1} x {n2} = {res}')
