print("Iniciando execução.")
maior = 0
menor = 0
while True:
    num = int(input("Informe um número: "))
    if num < 0:
        break
    if menor == 0:
        menor = num
    if num >= maior:
        maior = num
    elif num <= menor:
        menor = num
print(f'O maior valor inserido foi {maior} e o menor valor foi {menor}.')
