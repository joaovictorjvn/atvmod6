import sys

ano = int(input("Informe o ano atual: "))
aum = 0.015
sal = 2000
if ano < 1995:
    sys.exit("Dados inválidos. O funcionário foi contratado em 1995.")
for n in range(1995, ano + 1):
    sal = sal + (sal * aum)
    aum = aum * 2
print(f'O salário do funcionário no ano de {ano} equivale a R$ {sal}')
