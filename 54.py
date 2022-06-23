import sys

num = int(input("Informe um número: "))
if num <= 1:
    sys.exit("Número Inválido. Insira um número maior do que 1. ")
condprimo = 0
for n in range(1, num + 1):
    if num % n == 0:
        condprimo = condprimo + 1
if condprimo == 2:
    print(f'O número informado {num} é um número primo.')
else:
    print(f'O número informado {num} não é um número primo.')
