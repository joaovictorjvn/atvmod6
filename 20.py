import sys

num = int(input("Iniciando execução.\n"
                "Para iniciar digite qualquer número.\n"
                "Para encerrar digite 1000.\n"))
qnp = 0
itrc = 0
if num == 1000:
    sys.exit()
while num != 1000:
    if num % 2 == 0:
        qnp = qnp + 1
    itrc = itrc + 1
    num = int(input("Deseja continuar?\n"
                    "Para cancelar digite '1000': "))
print(f'Foram lidos {itrc} números e foram encontrados {qnp} números pares.\n'
      f'(O número utilizado para cancelamento da execução não é incluso nas estatísticas)')
