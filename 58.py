ininter = int(input("Informe o início do intervalo: "))
fiminter = int(input("Informe o final do intervalo: "))
condprimo = 0
soma = 0
for num in range(fiminter - 1, ininter, -1):
    for c in range(1, fiminter + 1):
        if num % c == 0:
            condprimo = condprimo + 1
    if condprimo == 2:
        soma = soma + num
    condprimo = 0
print(f'No intervalo entre {ininter} e {fiminter} a soma dos números primos entre eles é {soma}.')
