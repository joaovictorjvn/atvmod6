num = int(input("Informe um número para a execução: "))
while num < 100 or num > 999:
    num = int(input("Número inválido, informe um número entre 100 e 999: "))
res = [int(a) for a in str(num)]
print(f'Mostando os algorismos dentro de {num} separadamente: {res}')
