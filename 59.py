hab = int(input("Informe a quantidade de habitantes: "))
kwh = float(input("Informe o valor Kw/h: R$ "))
print("Agora informe as especificações de cada habitante.")
somares = 0
somacomerial = 0
somaind = 0
auxmaior = 0
auxmenor = 0
maior = 0
menor = 0
for n in range(1, hab + 1):
    consmensalkwh = float(input(f'Informe o consumo mensal do habitante {n}: '))
    cod = input(f'Informe o código do consumidor do habitante {n}\n'
                f'1 - Residencial\n'
                f'2 - Comercial\n'
                f'3 - Industrial\n')
    if consmensalkwh >= auxmaior:
        maior = n
        auxmaior = consmensalkwh
    if consmensalkwh <= auxmenor or auxmenor == 0:
        menor = n
        auxmenor = consmensalkwh
    if cod == '1':
        somares = somares + consmensalkwh
    elif cod == '2':
        somacomerial = somacomerial + consmensalkwh
    elif cod == '3':
        somaind = somaind + consmensalkwh
    else:
        print("Código Inválido.")
print(f'Relatório:\n'
      f'Maior consumidor: Habitante {maior} - Consumo {auxmaior} Kw.\n'
      f'Menor consumidor: Habitante {menor} - Consumo {auxmenor} Kw.\n'
      f'Média de Consumo: {(somaind + somacomerial + somaind) / hab} Kw.\n'
      f'Consumo total residencial: {somares} Kw.\n'
      f'Consumo total comercial: {somacomerial} Kw.\n'
      f'Consumo total industrial: {somaind} Kw.')
