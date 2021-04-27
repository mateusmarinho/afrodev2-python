'''Ler 3 valores (considerar que não serão iguais entre si) e escrever a soma dos
2 maiores valores'''


def is_int(valor):
    try:
        int(valor)
    except:
        return False

    return True


if __name__ == '__main__':
    cont = 0
    while cont < 3:
        valido = False
        while not valido:
            n = input(f'Digite o {cont + 1}º número: ')
            valido = is_int(n)
            if not valido:
                print('Valor inválido!')
        n = int(n)
        cont += 1

        if cont == 1:
            maior1 = n
        elif cont == 2:
            if n > maior1:
                maior2 = maior1
                maior1 = n
            else:
                maior2 = n
        else:
            if n > maior1:
                maior2 = maior1
                maior1 = n
            else:
                if n > maior2:
                    maior2 = n

    soma = maior1 + maior2
    print(f'A soma dos dois maiores números digitados é: {maior1} + {maior2} = {soma}')