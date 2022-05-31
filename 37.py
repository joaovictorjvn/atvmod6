print("Iniciando execução.")
res = 0
aux1 = 0
aux2 = 0
print("Mostrando números de 1000 a 9999 com a propriedade desejada pelo enunciado:")
for num in range(1000, 10000):
    res = [int(a) for a in str(num)]
    aux1 = (res[0] * 10) + res[1]
    aux2 = (res[2] * 10) + res[3]
    if (aux1 + aux2) ** 2 == num:
        print(num)
