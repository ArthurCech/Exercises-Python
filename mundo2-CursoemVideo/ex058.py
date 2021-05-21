# melhore o jogo do exercício 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

from random import randint

computer_number = randint(0, 10)

correct = False
hunches = 0

while not correct:
    user_number = int(input('digite o número (entre 0 e 10): '))
    hunches += 1

    if user_number == computer_number:
        correct = True
    elif user_number < computer_number:
        print('tente um número maior')
    else:
        print('tente um número menor')

print('Você acertou o número com {} tentativas'.format(hunches))
