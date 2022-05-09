import sys

lim = int(input("Informe um número ímpar: "))
if lim % 2 == 0:
    sys.exit("Número par inserido. Reinicie o programa.")
print(f'Mostrando números pares de 0 até {lim} em ordem crescente:')
for num in range(1, lim + 1, 2):
    print(num)
