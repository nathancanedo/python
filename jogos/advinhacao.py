import random

print('***********************************')
print("Bem vindo ao jogo de adivinhação")
print('***********************************')

print('')
dificuldade = int(input('Selecione a dificuldade: \n Fácil (1) Médio (2) Difícil (3) \n'))
print('')

nome_dificuldade = ''
total_de_tentativas = 0
pontos = 1000

if dificuldade == 1:
    total_de_tentativas = 10
    nome_dificuldade = 'Fácil'
elif dificuldade == 2:
    total_de_tentativas = 8
    nome_dificuldade = 'Médio'
elif dificuldade == 3:
    total_de_tentativas = 5
    nome_dificuldade = 'Difícil'
else:
    print('[ERRO] Você não digitou uma dificuldade válida!')
    exit()

erros = total_de_tentativas
numero_secreto = random.randrange(1, 101)

print('O jogo começou! 🏁')
print(f'Você está jogando no modo {nome_dificuldade.upper()}')

for rodada in range(1, total_de_tentativas + 1):
    print('')
    print('Tentativa: {} de {}'.format(rodada, total_de_tentativas))
    chute = int(input('Digite um número entre 1 e 100: '))
    print('Você digitou', chute)
    print('')

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
        print(f'Você fez {pontos} pontos!')
        print('🏆🏆🏆🏆🏆🏆🏆')

        break
    else:
        erros -= 1
        pontos -= chute
        if maior:
            print(f'Você errou! O número secreto é MENOR que {chute}!')
        elif menor:
            print(f'Você errou! O número secreto é MAIOR que {chute}!')

if erros == 0:
    print('')
    print('❌❌❌❌❌')
    print('Você perdeu!')
    print('❌❌❌❌❌')

print('')
print('-------------')
print('Fim de jogo')
print(f'O número secreto era {numero_secreto}')
print('-------------')
