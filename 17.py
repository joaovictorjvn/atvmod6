quant = int(input("Informe a quantidade de números a ser somada: "))
soma = 0
for num in range(0, quant):
    soma = num + soma
print(f'A soma dos {quant} primeiros números naturais partindo de 0 é {soma}.')
