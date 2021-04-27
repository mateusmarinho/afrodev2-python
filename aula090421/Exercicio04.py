'''Fazer um algoritmo para identificar se um aluno passou de ano dada a nota e o número
de faltas: nota entre 0 e 6 ou faltas maior que 9 então Reprovado, nota entre 6 e 8 e faltas
menor que 10 então Aprovado com restrição, nota entre 8 e 10 e falta menor que 15 então Aprovado,
nota 10 então aprovado com mérito'''


def is_float(valor):
    try:
        float(valor)
    except:
        return False

    return True


def is_int(valor):
    try:
        int(valor)
    except:
        return False

    return True


if __name__ == '__main__':
    valido = False
    while not valido:
        nota = input('Digite a nota: ')
        if is_float(nota) and 0 <= float(nota) <= 10:
            valido = True
        else:
            print('Nota inválida!')
    nota = float(nota)

    valido = False
    while not valido:
        faltas = input('Digite a quantidade de faltas: ')
        valido = is_int(faltas)
        if not valido:
            print('Valor inválido!')
    faltas = int(faltas)

    if nota == 10:
        print('Aprovado com mérito.')
    elif nota >= 8 and faltas < 15:
        print('Aprovado.')
    elif nota >= 6 and faltas < 10:
        print('Aprovado com restrição.')
    else:
        print('Reprovado.')
