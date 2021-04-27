'''Criar um algoritmo que leia um número diferente de zero e diga se este número é positivo
ou negativo'''


def is_int(valor):
    try:
        int(valor)
    except:
        return False

    return True


if __name__ == '__main__':
    # ANTES
    # num = int(input())
    #
    # while num == 0:
    #     num = int(input())
    #
    # if num > 0:
    #     print('O número digitado é positivo.')
    # else:
    #     print('O número digitado é negativo.')

    # DEPOIS
    num = input('Digite um número: ')

    while is_int(num) == False or int(num) == 0:
        print('Valor inválido!')
        if num == '0':
            print('Digite um número diferente de zero!')
        num = input('Digite um número: ')
    num = int(num)

    if num > 0:
        print('O número digitado é positivo.')
    else:
        print('O número digitado é negativo.')
