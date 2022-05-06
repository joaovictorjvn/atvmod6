print("Insira os 10 números para realizar a execução:")
cont = 1
auxh = 0
auxl = 0
while cont <= 10:
    num = int(input())
    if num >= auxh:
        auxh = num
    if auxl == 0:
        auxl = num
    elif num <= auxl:
        auxl = num
    cont = cont + 1
print(f'O menor valor é {auxl} e o maior valor é {auxh}.')
