from num2words import num2words

soma = 0
for num in range(1, 1001):
    npt = num2words(num, lang='pt-br')
    soma = soma + len(npt)
    for c in range(0, len(npt)):
        if npt[c] == ' ':
            soma = soma - 1
print(f'A soma das letras dos números de 1 a 1000 escritas por extenso é {soma}')
