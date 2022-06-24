print("Iniciando execução.")
num1 = 0
num2 = 0
maior = 0
for n in range(100, 1000):
    for c in range(999, 99, -1):
        palindromo = n * c
        res = [int(a) for a in str(palindromo)]
        if len(res) == 5:
            if res[4] == res[0] and res[3] == res[1]:
                maior = palindromo
        else:
            if res[5] == res[0] and res[4] == res[1] and res[3] == res[2]:
                if palindromo >= maior:
                    maior = palindromo
                    num1 = n
                    num2 = c
print(f'O maior palíndromo encontrado entre o produto de dois números de três digitos '
      f'sendo eles {num1} e {num2} é {maior}.')
