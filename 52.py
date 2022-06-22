import sys

saque = float(input("Informe o valor do saque: R$ "))
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
m1 = 0
if saque <= 0:
    sys.exit("Dados Inválidos.")
while saque > 0:
    if saque >= 100:
        saque = saque - 100
        n100 = n100 + 1
    elif saque >= 50:
        saque = saque - 50
        n50 = n50 + 1
    elif saque >= 20:
        saque = saque - 20
        n20 = n20 + 1
    elif saque >= 10:
        saque = saque - 10
        n10 = n10 + 1
    elif saque >= 5:
        saque = saque - 5
        n5 = n5 + 1
    elif saque >= 2:
        saque = saque - 2
        n2 = n2 + 1
    elif saque >= 1:
        saque = saque - 1
        m1 = m1 + 1
print(f'Foram necessárias {n100 + n50 + n20 + n10 + n5 + n2} cédula(s) e {m1} moeda(s), \n'
      f'dispostas da seguinte forma:\n{n100} notas de R$ 100\n'
      f'{n50} notas de R$ 50\n'
      f'{n20} notas de R$ 20\n'
      f'{n10} notas de R$ 10\n'
      f'{n5} notas de R$ 5\n'
      f'{n2} notas de R$ 2 e\n'
      f'{m1} moedas de R$ 1')
