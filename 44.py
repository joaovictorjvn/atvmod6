num = int(input("Informe um número: "))
fibo = 0
aux1 = 0
aux2 = 1
print(f'Mostrando sequência de fibonacci até o primeiro número maior do que {num}')
print(f'{aux2}', end=" ")
while fibo <= num:
    fibo = aux1 + aux2
    aux1 = aux2
    aux2 = fibo
    print(f'{fibo}', end=" ")
