quant = int(input("Informe a quantidade de números a ser mostrada: "))
print(f'Mostrando os {quant} primeiros números ímpares: ')
for num in range(1, quant * 2 + 1):
    if num % 2 != 0:
        print(num)
