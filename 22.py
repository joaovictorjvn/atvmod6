import sys

continuekey = 1
soma = 0
cont = 0
while continuekey > 0:
    print("Informe uma nota para o cálculo da média:")
    nota = int(input())
    if nota < 10 or nota > 20:
        sys.exit("Dados Inválidos inseridos.")
    else:
        soma = soma + nota
        cont = cont + 1
        continuekey = int(input("Deseja inserir outros valores?\n"
                                "Para continuar digite 1 e para cancelar digite 0.\n"))
print(f'A média aritmética das notas inseridas é {soma / cont}.')
