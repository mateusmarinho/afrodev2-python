'''Fazer um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o
preço unitário. Calcular e escrever o total (total = quantidade * preço unitário), o desconto
e o total a pagar (total a pagar = total - desconto), sabendo-se que:
- Se quantidade <= 5: desconto de 2%
- Se 5 < quantidade <= 10: desconto de 3%
- Se quantidade > 10: desconto de 5%'''


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
        produto = input('Digite o nome do produto: ')
        if produto != '':
            valido = True

    valido = False
    while not valido:
        quant = input('Digite a quantidade: ')
        if is_int(quant) and int(quant) > 0:
            valido = True
        else:
            print('Digite um valor numérico válido e maior que zero!')
    quant = int(quant)

    valido = False
    while not valido:
        preco = input('Informe o preço unitário: R$ ')
        if is_float(preco) and float(preco) > 0:
            valido = True
        else:
            print('Valor inválido!')
    preco = float(preco)

    total = quant * preco

    if quant <= 5:
        desconto = 2
    elif quant <= 10:
        desconto = 3
    else:
        desconto = 5

    total_pag = (1 - desconto / 100) * total

    print(f'Total da compra: R$ {total:.2f}\nTotal a pagar: R$ {total_pag:.2f}')
