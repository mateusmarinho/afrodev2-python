'''Fazer um algoritmo de uma lâmpada de emergência. A partir de um sinal, indique se a luz
está acesa ou apagada'''


def is_int(valor):
    try:
        int(valor)
    except:
        return False

    return True


if __name__ == '__main__':
    print('A lâmpada de emergência está apagada')
    sinal = 1

    saida = False
    while not saida:
        valido = False
        while not valido:
            sinal = input('Digite um sinal numérico [1]sistema ligado [0]sistema desligado [-1]encerrar: ')
            if is_int(sinal) and -1 <= int(sinal) <= 1:
                valido = True
        sinal = int(sinal)

        # se o sinal é maior que 0, o sistema de energia está ligado
        # se o sinal é menor ou igual a 0, o sistema de energia está desligado
        if sinal == 1:
            print('A lâmpada de emergência está apagada')
        elif sinal == 0:
            print('A lâmpada de emergência está acesa')
        else:
            print('ENCERRANDO...')
            saida = True
