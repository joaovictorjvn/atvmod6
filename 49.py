salc = float(input("Informe o salário de Carlos: R$ "))
salj = round(salc * (1 / 3), 10)
meses = 0
rendc = 0
rendj = 0
while True:
    lucroc = salc * 0.02
    lucroj = salj * 0.05
    rendc = round(rendc + lucroc, 10)
    rendj = round(rendj + lucroj, 10)
    salc = salc + rendc
    salj = salj + rendj
    if salj >= salc:
        print(f'Foram necessários {meses} meses para João alcançar o patrimônio de Carlos.')
        break
    else:
        meses = meses + 1
