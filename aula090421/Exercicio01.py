'''Somar 2 números e dividir por 2 se a soma for maior que 10 ou igual a 6'''


def is_int(valor):
    try:
        int(valor)
    except:
        return False

    return True


if __name__ == '__main__':
    valido = False
    while not valido:
        n1 = input('Digite o primeiro número: ')
        valido = is_int(n1)
        if not valido:
            print('Valor inválido!')
    n1 = int(n1)

    valido = False
    while not valido:
        n2 = input('Digite o segundo número: ')
        valido = is_int(n2)
        if not valido:
            print('Valor inválido!')
    n2 = int(n2)

    soma = n1 + n2

    if soma > 10 or soma == 6:
        resultado = soma / 2
    else:
        resultado = soma

    print(f'Soma = {soma} / Resultado final = {resultado}')
