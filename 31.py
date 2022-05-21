print("Iniciando a execução.")
s = 0
den = 1
for num in range(1, 100, 2):
    while den <= 50:
        s = s + (num / den)
        den = den + 1
        break
print(f'S = {s}')
