'''Ler 10 valores, calcular e escrever a média aritmética dos valores lidos'''


def is_float(valor):
    try:
        float(valor)
    except:
        return False

    return True


if __name__ == '__main__':
    cont = 0
    soma = 0
    while cont < 10:
        valido = False
        while not valido:
            n = input(f'Digite o {cont + 1}º valor: ')
            valido = is_float(n)
            if not valido:
                print('Valor inválido!')
        n = float(n)
        cont += 1
        soma += n

    media = soma / 10
    print(f'A média aritmética dos valores lidos é {media:.2f}')
