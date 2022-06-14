op = 0
while op != 5:
    op = int(input("Informe a opção desejada:\n"
                   "1 - Soma\n"
                   "2 - Subtração(Maior pelo menor)\n"
                   "3 - Multiplicação\n"
                   "4 - Divisão(Denominador não pode ser 0)\n"
                   "5 - Sair\n"))
    if op == 1:
        num1 = int(input("Informe o primeiro número para a operação: "))
        num2 = int(input("Informe o segundo número para a operação: "))
        print(f'A soma dos números inseridos equivale a {num1 + num2}')
    elif op == 2:
        num1 = int(input("Informe o primeiro número para a operação: "))
        num2 = int(input("Informe o segundo número para a operação: "))
        if num1 >= num2:
            print(f'A subtração dos números inseridos equivale a {num1 - num2}')
        else:
            print(f'A subtração dos números inseridos equivale a {num2 - num1}')
    elif op == 3:
        num1 = int(input("Informe o primeiro número para a operação: "))
        num2 = int(input("Informe o segundo número para a operação: "))
        print(f'A multiplicação dos números inseridos equivale a {num1 * num2}')
    elif op == 4:
        num1 = int(input("Informe o primeiro número para a operação(Numerador): "))
        num2 = int(input("Informe o segundo número para a operação(Denominador): "))
        if num2 == 0:
            print("Não é possível dividir por 0.")
        else:
            print(f'A divisão dos números inseridos equivale a {num1 / num2}')
    elif op == 5:
        break
    else:
        print("Opção inválida.")
