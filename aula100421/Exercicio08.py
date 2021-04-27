'''Fazer um algoritmo para imprimir a tabuada do valor inserido'''


def is_int(valor):
    try:
        int(valor)
    except:
        return False

    return True


if __name__ == '__main__':
    valido = False
    while not valido:
        valor = input('Digite um valor para calcular a tabuada: ')
        if is_int(valor) and int(valor) > 0:
            valido = True
        else:
            print('Valor inválido')
    valor = int(valor)

    mult = 1
    while mult <= 10:
        res = valor * mult
        print(f'{valor} x {mult} = {res}')
        mult += 1
