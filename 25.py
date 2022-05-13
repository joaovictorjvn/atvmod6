print("Iniciando execução.")
soma = 0
for n in range(1000, 0, -1):
    if n % 3 == 0 or n % 5 == 0:
        soma = soma + n
print(f'A soma dos números múltiplos de 3 ou 5 de 1000 até 0 é {soma}')
