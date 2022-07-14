def titulo(txt):
    print('-=' * 15)
    print(txt)
    print('-=' * 15)
def totarea(n1, n2):
    res = n1 * n2
    print('-=' * 30)
    print(f'A área total de um terreno {n1} x {n2} é de {res}')
    print('-=' * 30)


titulo('Controle de terreno')
totarea(
    n1=float(input('Largura (m): ')),
    n2=float(input('Comprimento (m): '))
)