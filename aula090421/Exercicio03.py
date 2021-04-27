'''Fazer um algoritmo para verificar se o número é maior que 10 e par'''


def is_int(valor):
    try:
        int(valor)
    except:
        return False

    return True


if __name__ == '__main__':
    valido = False
    while not valido:
        num = input('Digite um número: ')
        if is_int(num) and int(num) > 0:
            valido = True
    num = int(num)

    if num > 10:
        print(f'{num} é maior que 10.')
    else:
        print(f'{num} não é maior que 10.')

    if num % 2 == 0:
        print(f'{num} é par.')
    else:
        print(f'{num} não é par.')


