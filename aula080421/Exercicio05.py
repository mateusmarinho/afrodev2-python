'''Escrever um algoritmo para ler o número de votos brancos, nulos e válidos. Calcular e escrever o
percentual que cada um representa em relação ao total de eleitores (supondo que todos os eleitores
de uma cidade votaram)'''


def is_int(valor):
    try:
        int(valor)
    except:
        return False

    return True


if __name__ == '__main__':
    # ANTES
    # vb = input()
    # while is_int(vb) == False or int(vb) < 0:
    #     vb = input()
    # vb = int(vb)
    #
    # vn = input()
    # while is_int(vn) == False or int(vn) < 0:
    #     vn = input()
    # vn = int(vn)
    #
    # vv = input()
    # while is_int(vv) == False or int(vv) < 0:
    #     vv = input()
    # vv = int(vv)
    #
    # total = vb + vn + vv
    # perc_b = (vb / total) * 100
    # perc_n = (vn / total) * 100
    # perc_v = (vv / total) * 100
    #
    # print(perc_b)
    # print(perc_n)
    # print(perc_v)

    # DEPOIS
    v_brancos = input('Digite a quantidade de votos brancos: ')
    while is_int(v_brancos) == False or int(v_brancos) < 0:
        print('Valor inválido!')
        v_brancos = input('Digite a quantidade de votos brancos: ')
    v_brancos = int(v_brancos)

    v_nulos = input('Digite a quantidade de votos nulos: ')
    while is_int(v_nulos) == False or int(v_nulos) < 0:
        print('Valor inválido!')
        v_nulos = input('Digite a quantidade de votos nulos: ')
    v_nulos = int(v_nulos)

    v_validos = input('Digite a quantidade de votos válidos: ')
    while is_int(v_validos) == False or int(v_validos) < 0:
        print('Valor inválido!')
        v_validos = input('Digite a quantidade de votos válidos: ')
    v_validos = int(v_validos)

    total = v_brancos + v_nulos + v_validos
    p_brancos = (v_brancos / total) * 100
    p_nulos = (v_nulos / total) * 100
    p_validos = (v_validos / total) * 100

    print(f'Porcentagem de votos brancos: {p_brancos:.2f}%')
    print(f'Porcentagem de votos nulos: {p_nulos:.2f}%')
    print(f'Porcentagem de votos brancos: {p_validos:.2f}%')
