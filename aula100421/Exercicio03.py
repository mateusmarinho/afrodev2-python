'''As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem
compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcula e
escreva o custo total da compra'''


def is_int(valor):
    try:
        int(valor)
    except:
        return False

    return True


if __name__ == '__main__':
    valido = False
    while not valido:
        quant = input('Digite a quantidade de maçãs: ')
        if is_int(quant) and int(quant) > 0:
            valido = True
        else:
            print('Digite um valor numérico válido e maior que zero!')
    quant = int(quant)

    if quant < 12:
        print('Preço unitário: R$ 1,30')
        total = 1.30 * quant
    else:
        print('Preço unitário: R$ 1,00')
        total = 1.00 * quant

    print(f'Total da compra: R$ {total:.2f}')
