# melhore o jogo do exer028 onde o computador vai "pensar" em um número entre 0 e 10. Só 
# que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites 
# foram necessários para vencer

from random import randint
from time import sleep

numberComputer = randint(0, 10)

attempts = 0
correct = False
while not correct:
    numberUser = int(input('digite um número entre 0 e 10: '))
    print('PROCESSANDO...')
    sleep(1)
    
    attempts += 1

    if numberUser == numberComputer:
        correct = True
    elif numberUser < numberComputer:
        print('O número é maior')
    elif numberUser > numberComputer:
        print('O número é menor')

print('\033[1;32mVocê acertou!\033[m')
print('\033[1;33mTentativas: {}\033[m'.format(attempts))
