import sys

lim = int(input("Informe o número limite: "))
i = int(input("Informe um número inteiro e positivo: "))
j = int(input("Informe outro número inteiro e positivo: "))
if i <= 0 or j <= 0 or lim < 0:
    sys.exit("Dados Inválidos.")
print(f'Mostrando números múltiplos de {i}, {j} ou ambos em ordem crecente até o limite {lim}:')
for n in range(0, lim + 1):
    if n % i == 0 or n % j == 0:
        print(n)
