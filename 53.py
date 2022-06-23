linhas = int(input("Informe o número de linhas: "))

m = 1
for c in range(1, linhas + 1):
    for i in range(1, c + 1):
        print(m, end=' ')
        m += 1
    print()
