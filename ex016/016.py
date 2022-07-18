from ex016 import moeda

preço = float(input('Digite o preço R$:'))
print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço, True)}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preço, True, 10)}')
print(f'Reduzindo 10%, temos {moeda.diminuir(preço, True, 10)}')