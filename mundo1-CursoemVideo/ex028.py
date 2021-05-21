# escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep

user_number = int(input('digite o número (entre 0 e 5): '))

computer_number = randint(0, 5)

print('PROCESSANDO...')
sleep(2)

if user_number == computer_number:
    print('O jogador acertou. O número era {}'.format(computer_number))
else:
    print('O jogador errou. O número era {}'.format(computer_number))
