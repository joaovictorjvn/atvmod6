print("Insira os números para o cálculo da média: ")
cont = 1
soma = 0
while cont <= 10:
    num = int(input())
    soma = soma + num
    cont = cont + 1
print(f'A média dos números inseridos é {soma / (cont - 1)}')
