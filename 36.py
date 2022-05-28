print("Iniciando a execução.")
soma = 0
for num in range(1, 101):
    soma = soma + (num ** 2)
print(f'A diferença da soma dos quadrados dos algorismos para\n'
      f'o quadrado da soma geral é {(soma ** 2) - soma}.')
