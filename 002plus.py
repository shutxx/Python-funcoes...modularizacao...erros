def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {larg} x {comp} é de {a}m².')


# programa principal
print('Controle de terrenos')
print('-' * 20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)