import sys

base = float(input("Informe a base do triângulo: "))
alt = float(input("Informe a altura do triângulo: "))
if base <= 0 or alt <= 0:
    sys.exit("Dados Inválidos.")
else:
    print(f'A área do triângulo é {(base * alt) / 2}')
