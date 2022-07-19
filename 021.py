def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um inteiro: ')
n2 = leiafloat('Digite um real: ')
print(f'O valor inteiro digitado voi {n1} e o valor real foi {n2}')