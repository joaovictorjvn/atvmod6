import math

print("Iniciando a execução.")
res = 0
den = 2
for num in range(1, 6):
    while den <= 10:
        res = num / (math.factorial(den))
        den = den + 2
        break
print(f'O resultado desejado é {res}')
