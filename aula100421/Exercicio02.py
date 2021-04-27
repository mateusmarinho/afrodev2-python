'''Ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e escrever
se formam ou não um triângulo'''


def is_float(valor):
    try:
        float(valor)
    except:
        return False

    return True


if __name__ == '__main__':
    print('Verificação de triângulo')

    valido = False
    while not valido:
        ladoA = input('Digite a medida do primeiro lado (A): ')
        if is_float(ladoA) and float(ladoA) > 0:
            valido = True
        else:
            print('Digite um valor numérico válido e maior que zero!')
    ladoA = float(ladoA)

    valido = False
    while not valido:
        ladoB = input('Digite a medida do segundo lado (B): ')
        if is_float(ladoB) and float(ladoB) > 0:
            valido = True
        else:
            print('Digite um valor numérico válido e maior que zero!')
    ladoB = float(ladoB)

    valido = False
    while not valido:
        ladoC = input('Digite a medida do terceiro lado (C): ')
        if is_float(ladoC) and float(ladoC) > 0:
            valido = True
        else:
            print('Digite um valor numérico válido e maior que zero!')
    ladoC = float(ladoC)

    if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:
        print('As medidas digitadas formam um triângulo.')
    else:
        print('As medidas digitadas NÃO formam um triângulo.')
