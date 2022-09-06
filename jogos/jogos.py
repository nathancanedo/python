import forca
import adivinhacao

print('***********************************')
print('Bem vindo a Central de Jogos')
print('***********************************')
print('')
print('Escolha um Jogo:')
print('(1) Forca (2) Adivinhação')
jogo = int(input('Faça a sua escolha:'))

if jogo == 1:
    print('Iniciando Forca...')
    forca.jogar()
elif jogo == 2:
    print('Iniciando Adivinhação...')
    adivinhacao.jogar()