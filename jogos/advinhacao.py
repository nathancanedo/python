print('***********************************')
print("Bem vindo ao jogo de adivinhação")
print('***********************************')

numero_secreto = 42
total_de_tentativas = 3
tentativa_atual = total_de_tentativas
rodada = 0

while tentativa_atual > 0:
    rodada += 1
    print('Tentativa:', rodada, 'de', total_de_tentativas)
    chute = int(input('Digite um número: '))
    print('Você digitou', chute)

    tentativa_atual -= 1

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
print('-------------')
