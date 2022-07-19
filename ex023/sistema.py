from ex023.lib.interface import *
from ex023.lib.arquivos import *
from time import sleep

arq = 'pessoas.txt'
if not arquivoExiste(arq):
    CriarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # opção de cadastrar uma nova pessoa
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema')
        break
    else:
        print('\033[31mERRO! Digite uma opçao valida.\033[m')
    sleep(2)
