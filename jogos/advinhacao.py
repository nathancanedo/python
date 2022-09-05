import random

print('***********************************')
print("Bem vindo ao jogo de adivinhação")
print('***********************************')

numero_secreto = int
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print('Tentativa: {} de {}'.format(rodada, total_de_tentativas))
    chute = int(input('Digite um número entre 1 e 100: '))
    print('Você digitou', chute)

    if chute < 1 or chute > 100:
        print('[ERRO] Você deve digitar um número entre 1 e 100!')
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('Você acertou!')
        break
    else:
        if maior:
            print('Você errou! Seu chute foi MAIOR que o número secreto!')
        elif menor:
            print('Você errou! Seu chute foi MENOR que o número secreto!')

print('')
print('-------------')
print('Fim de jogo')
print(f'O número era {numero_secreto}')
print('-------------')
