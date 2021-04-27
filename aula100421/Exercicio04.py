'''Fazer um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após,
calcular e escrever o saldo atual (saldo + crédito - débito). Se o saldo atual for maior ou
igual a zero, escrever a mensagem "Saldo Positivo", senão escrever a mensagem "Saldo Negativo".'''


def is_int(valor):
    try:
        int(valor)
    except:
        return False

    return True


def is_float(valor):
    try:
        float(valor)
    except:
        return False

    return True


if __name__ == '__main__':
    valido = False
    while not valido:
        conta = input('Digite a conta do cliente: ')
        if is_int(conta) and int(conta) > 0:
            valido = True
        else:
            print('Conta inválida! Digite o ID numérico.')
    conta = int(conta)

    valido = False
    while not valido:
        saldo = input('Digite o saldo do cliente: R$ ')
        valido = is_float(saldo)
        if not valido:
            print('Valor inválido!')
    saldo = float(saldo)

    valido = False
    while not valido:
        deb = input('Informe o valor do débito: R$ ')
        if is_float(deb) and float(deb) > 0:
            valido = True
        else:
            print('Valor inválido!')
    deb = float(deb)

    valido = False
    while not valido:
        cred = input('Informe o valor do crédito: R$ ')
        if is_float(cred) and float(cred) > 0:
            valido = True
        else:
            print('Valor inválido!')
    cred = float(cred)

    saldo_atual = saldo - deb + cred

    print(f'Conta: {conta}\nSaldo atual: R$ {saldo_atual:.2f}')

    if saldo_atual < 0:
        print('Saldo Negativo')
    else:
        print('Saldo Positivo')