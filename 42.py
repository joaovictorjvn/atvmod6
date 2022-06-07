print("Para finalizar digite '0' ou algum número negativo.")
while True:
    num = int(input("Informe um número: "))
    if num <= 0:
        break
    else:
        print(f'{num}² = {num ** 2}')
        print(f'{num}³ = {num ** 3}')
        print(f'v{num} = {num ** 0.5}')
