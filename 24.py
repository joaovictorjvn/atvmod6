"""
O enunciado pede por números inteiros, porém nesse programa apenas inteiros positivos serão
utlizados, pois se os números negativos fossem contabilizados a soma dos divisores sempre será
'0'.
"""
import sys

num = int(input("Informe um número: "))
soma = 0
if num <= 0:
    sys.exit("Número Inválido.")
else:
    for n in range(num - 1, 0, -1):
        if num % n == 0:
            soma = soma + n
print(f'A soma dos divisores de {num} é {soma}')
