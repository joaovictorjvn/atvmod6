import sys

n = int(input("Informe um número: "))
if n <= 0:
    sys.exit("Número Inválido.")
harm = 0
for den in range(1, n + 1):
    harm = harm + (1 / den)
print(f'H(n) = {harm}')
