num = int(input("Informe um número: "))
while True:
    if num % 11 == 0 or num % 13 == 0 or num % 17 == 0:
        print(f'O primeiro número a partir do número inicial múltiplo de 11, 13 ou 17 é {num}')
        break
    else:
        num = num + 1
