from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.5)
    print('Pronto')

def maior(lista):
    c = maior = 0
    print('-=' * 20)
    print('Analisando os valores...')
    print('-=' * 20)
    for valor in lista:
        print(f'{valor}', end=' ')
        sleep(0.5)
        if c == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        c += 1

    print(f'\nForam informados {c} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


numeros = list()
sorteia(numeros)
maior(numeros)
