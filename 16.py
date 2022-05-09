import sys

lim = int(input("Informe um número ímpar: "))
if lim % 2 == 0:
    sys.exit("Número par inserido. Reinicie o programa.")
print(f'Mostrando números pares de 0 até {lim} em ordem decrescente:')
for num in range(lim, 0, -2):
    print(num)
