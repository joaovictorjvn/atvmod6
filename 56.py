print("Iniciando execução.")
condprimo = 0
soma = 0
for num in range(2_000_000, 0, -1):
    for c in range(1, 2_000_001):
        if num % c == 0:
            condprimo = condprimo + 1
    if condprimo == 2:
        soma = soma + 1
    condprimo = 0
print(f'A soma dos números primos até o número 2000000(Dois milhões) é {soma}.')
