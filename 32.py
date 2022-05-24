import random

lan = int(input("Informe a quantidade de lançamentos: "))
cont = 1
while cont <= 5:
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    print(f'Dado 1: {d1}')
    print(f'Dado 2: {d2}')
    if d1 > d2:
        print(f'Dado 1 tem o maior valor.')
    elif d2 > d1:
        print(f'Dado 2 tem o maior valor.')
    else:
        print(f'Os dados tem valor igual.')
    cont = cont + 1
