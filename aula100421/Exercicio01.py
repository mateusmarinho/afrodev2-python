'''Escrever um algoritmo para ler as dimensões de um retângulo (base e altura), calcular
e escrever a área do retângulo'''


def is_float(valor):
    try:
        float(valor)
    except:
        return False

    return True


if __name__ == '__main__':
    print('Área do retângulo')

    valido = False
    while not valido:
        base = input('Digite a medida da base: ')
        if is_float(base) and float(base) > 0:
            valido = True
        else:
            print('Digite um valor numérico válido e maior que zero!')
    base = float(base)

    valido = False
    while not valido:
        altura = input('Digite a medida da altura: ')
        if is_float(altura) and float(altura) > 0:
            valido = True
        else:
            print('Digite um valor numérico válido e maior que zero!')
    altura = float(altura)

    area = base * altura

    print(f'A área do retangulo é igual a {area:.2f} u.a.')
