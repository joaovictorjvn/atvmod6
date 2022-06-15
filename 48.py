print("Iniciando execução.")
fibo = 0
aux1 = 0
aux2 = 1
soma = 0
while fibo <= 4_000_000:
    fibo = aux1 + aux2
    aux1 = aux2
    aux2 = fibo
    if fibo % 2 == 0:
        soma = soma + fibo
print(f'A soma dos números pares da sequência de Fibonacci mernores que 4000000 é {soma}')
