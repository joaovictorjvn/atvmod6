import sys

num = int(input("Informe um número: "))
if num <= 0:
    sys.exit("Dados Inválidos. Informe um número maior que 0.")
condprimo = 0
soma = 0
quant = 0
for n in range(1, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000):
    if quant == num:
        break
    for c in range(n, 0, -1):
        if n % c == 0:
            condprimo = condprimo + 1
    if condprimo == 2:
        soma = soma + n
        quant = quant + 1
    condprimo = 0
print(f'A soma dos {num} primeiros números primos é {soma}')
