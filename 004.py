from time import sleep
def conti(cont):
    for cont in range(1, 11):
        print(cont, end=', ')
        sleep(0.5)
def regres(com):
    for com in range(10, -1, -2):
        print(com, end=', ')
        sleep(0.5)
def contador(i, f, p):
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    for c in range(i, f, p):
        print(c, end=', ')
        sleep(0.2)


# programa principal
print('-=' * 20)
print('Contagem de 1 até 10 de 1 em 1')
sleep(1.5)
conti(conti)
print()
print('-=' * 20)
print('Contagem de 10 até 0 de 2 em 2')
sleep(1.5)
regres(regres)
print()
print('-=' * 20)
print('Contagem personalizada')
inicio = int(input('Inicio: '))
fim =int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)