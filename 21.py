num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
soma = 0
mult = 1
if num1 > num2:
    for num in range(num2, num1 + 1):
        if num % 2 == 0:
            soma = soma + num
        else:
            mult = mult * num
else:
    for num in range(num1, num2 + 1):
        if num % 2 == 0:
            soma = soma + num
        else:
            mult = mult * num
print(f'Entre os números {num1} e {num2} a soma dos números pares e multiplicação dos números'
      f' ímpares nesse intervalo equivale respectivamente a {soma} e {mult}')
