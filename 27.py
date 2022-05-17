n = int(input("Informe um número: "))
harm = 0
for den in range(1, n + 1):
    harm = harm + (1 / den)
print(f'H(n) = {harm}')
