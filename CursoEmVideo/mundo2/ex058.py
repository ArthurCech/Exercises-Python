# melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

from random import randint
from time import sleep

computer = randint(0, 10)

attempts = 0
correct = False

while not correct:
    user = int(input('digite um número entre 0 e 10: '))
    
    print('PROCESSANDO...')
    sleep(1)
    
    attempts += 1

    if user == computer:
        correct = True
    elif user < computer:
        print('O número é maior')
    elif user > computer:
        print('O número é menor')

print('Você acertou!')
print('Tentativas: {}'.format(attempts))
