import math

num = int(input("Informe um número: "))
e = 1
for n in range(1, num + 1):
    e = e + (1 / math.factorial(n))
print(f'E = {e}')
