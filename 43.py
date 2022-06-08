print("Para finalizar digite '0' na idade do indivíduo.")
soma = 0
quant = 0
while True:
    idade = int(input("Informe a idade do indivíduo: "))
    if idade <= 0:
        break
    soma = soma + idade
    quant = quant + 1
if soma == 0 or quant == 0:
    print("Nenhum valor inserido.")
else:
    print(f'A media das idades inseridas é {soma / quant}')
