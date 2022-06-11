import random

print("Iniciando o jogo.\nBoa sorte.\nTente advinhar o número.")
atempts = 1
goal = random.randint(1, 1000)
while True:
    guess = int(input("Qual é número?\n"))
    if guess > goal:
        print("Resposta incorreta.\nTente novamente.\nO número certo é menor do que o número "
              "que você inseriu.")
        atempts = atempts + 1
    elif guess < goal:
        print("Resposta incorreta.\nTente novamente.\nO número certo é maior do que o número "
              "que você inseriu.")
        atempts = atempts + 1
    else:
        print(f'Resposta correta.\nForam {atempts} tentativas ao todo.')
        break
