import sys

inicio = int(input("Informe o início do intervalo: "))
fim = int(input("Informe o fim do intervalo: "))
if inicio >= fim:
    sys.exit("Intervalo inválido.")
soma = 0
for n in range(inicio, fim + 1):
    if n % 2 != 0:
        soma = soma + n
print(f'A soma dos números ímpares no intervalo de {inicio} a {fim} é {soma}.')
