import sys

print("Iniciando Execução.")
a = 1
obj = 1000
while True:
    for b in range(1, 1001):
        c = (a ** 2 + b ** 2) ** 0.5
        if a + b + c == obj:
            print(f'O conjunto pitagórico no qual (a + b + c = 1000) é: a = {a}, b = {b} e c = {c}.')
            sys.exit()
    a = a + 1
