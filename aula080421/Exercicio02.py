'''Criar um algoritmo que receba 3 números e informe qual o maior entre eles'''


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
    # maior = n1
    #
    # n2 = input()
    # while is_int(n2) == False:
    #     n2 = input()
    # n2 = int(n2)
    #
    # if n2 > maior:
    #     maior = n2
    #
    # n3 = input()
    # while is_int(n3) == False:
    #     n3 = input()
    # n3 = int(n3)
    #
    # if n3 > maior:
    #     maior = n3
    #
    # print(maior)

    # DEPOIS
    cont = 0
    while cont < 3:
        n = input(f'Digite o {cont+1}º número: ')
        while is_int(n) == False:
            print('Valor inválido!')
            n = input(f'Digite o {cont+1}º número: ')
        n = int(n)
        cont += 1

        if cont == 1:
            maior = n
        else:
            if n > maior:
                maior = n

    print(f'O maior número digitado foi {maior}.')
