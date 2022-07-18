from ex019.utilidadesCeV import moeda
from ex019.utilidadesCeV import dados

preço = dados.leiaDinheiro('Digite o preço R$:')
moeda.resumo(preço, 35)