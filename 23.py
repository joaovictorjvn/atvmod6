import sys

num = int(input("Informe um número: "))
if num <= 0:
    sys.exit("Número Inválido.")
else:
    print(f'Os divisores de {num} são:')
    for n in range(num, 0, -1):
        if num % n == 0:
            print(n)
