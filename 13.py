import sys

lim = int(input("Informe um número par: "))
if lim % 2 != 0:
    sys.exit("Número ímpar inserido. Reinicie o programa.")
print(f'Mostrando números pares de 0 até {lim} em ordem crescente:')
for num in range(0, lim + 1, 2):
    print(num)
