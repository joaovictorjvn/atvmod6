quant = int(input("Informe a quantidade de números a ser lida: "))
cont = 0
mainu = 0
quantmainu = 1
print(f'Lendo os {quant} números desejados pelo usuário:')
while cont < quant:
    num = int(input())
    if num > mainu:
        mainu = num
        quantmainu = 1
    elif num == mainu:
        quantmainu = quantmainu + 1
    cont = cont + 1
print(f'O maior número é {mainu} e ele foi lido {quantmainu} vez(es).')
