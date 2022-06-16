salc = float(input("Informe o salário de Carlos: R$ "))
salj = round(salc * (1 / 3), 0)
meses = 1
lucroc = salc * 0.02
lucroj = salj * 0.05
rendc = 0
rendj = 0
while True:
    rendc = round(rendc + lucroc, 0)
    rendj = round(rendj + lucroj, 0)
    if (salj + rendj) >= (salc + rendc):
        print(f'Foram necessários {meses} meses para João alcançar o patrimônio de Carlos.')
        break
    else:
        meses = meses + 1
"""
Nota: O valor recebido por João é sempre menor do que o de Carlos, supondo que Carlos ganhe
R$ 1000 de salário, com essa informação sabe - se que o salário de João equivale a R$ 333(Arredondado),
com as respectivas taxas em questão Carlos receberia R$ 20 de renda todo mês e João R$ 17 ou seja, 
sempre um valor inferior, não estou considerando aumento de salário pois nada foi mencionado no enunciado,
mais ainda que fosse esse o caso, o valor do salário de João será incrementado, porém o de Carlos também será 
e como as taxas são fixas elas sempre serão nas mesmas proporções, impossibilitando assim que João alcance o
patrimônio de Carlos na situação oferecida pelo enunciado.
"""
