import random

print('***********************************')
print("Bem vindo ao jogo de adivinhação")
print('***********************************')
print('')
dificuldade = input('Selecione a dificuldade: \n Fácil (1) Médio (2) Difícil (3) \n')
print('')

total_de_tentativas = int()

if dificuldade == '1':
    total_de_tentativas = 10
elif dificuldade == '2':
    total_de_tentativas = 5
elif dificuldade == '3':
    total_de_tentativas = 3

numero_secreto = int(random.random()*101)

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
        print('')
        print('🏆🏆🏆🏆🏆🏆🏆')
        print('Você acertou!')
        print('🏆🏆🏆🏆🏆🏆🏆')

        break
    else:
        if maior:
            print(f'Você errou! O número secreto é MENOR que {chute}!')
        elif menor:
            print(f'Você errou! O número secreto é MAIOR que {chute}!')

print('')
print('-------------')
print('Fim de jogo')
print(f'O número secreto era {numero_secreto}')
print('-------------')
