'''◦Somar 2 números e dividir por um terceiro
◦Verificar se o terceiro é diferente de 0
◦Verificar se  primeiro valor é maior que 10
◦Verificar se resultado é  menor que 4'''


def askInt(text):
    while True:
        try:
            n = int(input(text))
        except:
            print('Valor inválido! Digite um número inteiro!')
            continue
        else:
            return n


def is_int(valor):
    try:
        int(valor)
    except:
        return False

    return True


if __name__ == '__main__':
    # ANTES
    # n1 = input()
    # while is_int(n1) == False and int(n1) <= 10:
    #     n1 = input()
    # n1 = int(n1)
    #
    # n2 = input()
    # while is_int(n2) == False:
    #     n2 = input()
    # n2 = int(n2)
    #
    # n3 = input()
    # while is_int(n3) == False and int(n3) == 10:
    #     n3 = input()
    # n3 = int(n3)
    #
    # soma = n1 + n2
    # resultado = soma / n3
    #
    # if resultado < 4:
    #     print('O resultado é menor que 4')

    # DEPOIS
    # while True:
    #     num1 = askInt('Digite o primeiro valor: ')
    #     if num1 > 10:
    #         break
    #     else:
    #         print('Digite um valor maior que 10')
    #
    # num2 = askInt('Digite o segundo valor: ')
    #
    # while True:
    #     num3 = askInt('Digite o terceiro valor: ')
    #     if num3 == 0:
    #         print('Digite um valor diferente de 0')
    #     else:
    #         break

    while True:
        num1 = input('Digite o primeiro valor: ')
        if is_int(num1) and int(num1) > 10:
            num1 = int(num1)
            break
        else:
            print('Valor inválido! Digite um número inteiro maior que 10.')

    while True:
        num2 = input('Digite o segundo valor: ')
        if is_int(num2):
            num2 = int(num2)
            break
        else:
            print('Valor inválido! Digite um número inteiro.')

    while True:
        num3 = input('Digite o terceiro valor: ')
        if is_int(num3) and int(num3) != 0:
            num3 = int(num3)
            break
        else:
            print('Valor inválido! Digite um número inteiro diferente de 0.')

    resultado = (num1 + num2) / num3

    print(f'O resultado da soma de {num1} e {num2} dividida por {num3} é igual a {resultado}')

    if resultado < 4:
        print('O resultado é menor que 4.')
    else:
        print('O resultado não é menor que 4.')
