op = 0
while op != 3:
    print("Informe a operação desejada:\n"
          "1 - Converter Km/h para m/s\n"
          "2 - Converter m/s para Km/h\n"
          "3 - Sair")
    op = int(input())
    if op == 1:
        valor = int(input("Informe a velocidade em Km/h para ser convertida: "))
        print(f'A velocidade informada em m/s é {valor / 3.6}')
    elif op == 2:
        valor = int(input("Informe a velocidade em m/s para ser convertida: "))
        print(f'A velocidade informada em Km/h é {valor * 3.6}')
    elif op == 3:
        break
    else:
        print("Opção Inválida.")
