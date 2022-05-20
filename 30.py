lim = int(input("Informe um limite para o cálculo das sequências: "))
seq = 0
seq2 = 0
seq3 = 0
for num in range(1, lim + 1):
    seq = seq + num
for num in range(1, lim + 1):
    seq2 = seq2 + (num - (num - 1))
for num in range(1, lim + 1, 2):
    seq3 = seq3 + num
print(f'O resultados das sequências ficou da seguinte forma:\n'
      f'Sequência 1 (n) = {seq}\n'
      f'Sequência 2 (n - (n -1)) = {seq2}\n'
      f'Sequência 3 (2n - 1) = {seq3}')
"""
Não compreendi muito bem a lógica da sequêcia 2, fiz o que achei correto de acordo com
o que vi no enunciado.
"""
