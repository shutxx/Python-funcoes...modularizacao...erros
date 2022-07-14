def titulo(txt):
   print('-=' * 15)
   print(txt)
   print('-=' * 15)
def soma(a, b):
   print(f'A = {a} e B = {b}')
   s = a + b
   print(f'A soma de A + B é = {s}')
   print('-=' * 15)
def dobra(lst):
   pos = 0
   while pos < len(lst):
      lst[pos] *= 2
      pos += 1
def soma1(* valores1):
   s = 0
   for num in valores1:
      s += num
   print(f'Somando os valores {valores1} temos {s}')


# programa principal
titulo('    curso de python     ')
soma(b=2, a=5)
soma(8, 8)
soma(2, 1)
# valores dobrados
valores = [7, 2, 5, 0, 4]
print(valores)
dobra(valores)
print(valores)
print('-=' * 15)
# desenpacota
soma1(5, 2)
soma1(2, 9, 4)
