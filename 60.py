print("Iniciando execução.\n"
      "Para finalizar insira o número 0.")
soma = 0
somapares = 0
quant = 0
maior = 0
menor = 0
num = 1
while num != 0:
    num = int(input("Informe um número: "))
    if num == 0:
        break
    if num >= maior:
        maior = num
    if num <= menor or menor == 0:
        menor = num
    if num % 2 == 0:
        somapares = somapares + num
    soma = soma + num
    quant = quant + 1
print(f'Mostrando itens:\n'
      f'Soma dos números digitados: {soma}\n'
      f'Quantidade de números digitados: {quant}\n'
      f'Média dos números digitados: {soma / quant}\n'
      f'Maior número digitado: {maior}\n'
      f'Menor número digitado: {menor}\n'
      f'Soma dos número pares digitados: {somapares}')
