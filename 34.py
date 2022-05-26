print("Iniciando execução.")
n = 1
nfinal = 0
print("Mostrando o número que é divisível por todos os números de 1 a 20(Com resto 0):")
while True:
    for num in range(1, 21):
        res = n % num
        if res == 0:
            nfinal = nfinal + 1
        else:
            nfinal = 0
            break
    if nfinal == 20:
        print(n)
        break
    else:
        n = n + 1
