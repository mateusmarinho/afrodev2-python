'''Exemplo de aula: utilização de caixinhas de diálogo'''

from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog


def is_int(n):
    try:
        int(n)
    except:
        return False

    return True


if __name__ == '__main__':
    root = Tk()
    root.withdraw()

    num1 = simpledialog.askinteger('Entrada', 'Digite o primeiro valor:')
    num2 = simpledialog.askinteger('Entrada', 'Digite o segundo valor:')

    soma = num1 + num2

    messagebox.showinfo('Saída', f'O resultado da soma é {soma}')

    # messagebox.showinfo('Bem-vindo/Bem-vinda', 'Digite dois números para calcular sua soma dividida por 2')
    #
    # inteiro = False
    # while inteiro == False:
    #     valor1 = input('Digite o primeiro valor: ')
    #     if is_int(valor1):
    #         valor1 = int(valor1)
    #         inteiro = True
    #     else:
    #         messagebox.showerror('Erro', 'Digite um número inteiro!')
    #
    # inteiro = False
    # while inteiro == False:
    #     valor2 = input('Digite o segundo valor: ')
    #     if is_int(valor2):
    #         valor2 = int(valor2)
    #         inteiro = True
    #     else:
    #         messagebox.showerror('Erro', 'Digite um número inteiro!')
    #
    # soma = valor1 + valor2
    # resultado = soma / 2
    # print(f'A soma de {valor1} e {valor2} dividida por 2 é igual a {resultado}')
