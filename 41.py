while True:
    r1 = int(input("Informe a resistência do primeiro resistor: "))
    r2 = int(input("Informe a resistência do segundo resistor: "))
    if r1 == 0 or r2 == 0:
        break
    r = (r1 * r2) / (r1 + r2)
    print(f'O valor do cálculo é {r}\n'
          f'Para finalizar a execução do programa insira o valor "0" em '
          f'qualquer uma das resistências.')
