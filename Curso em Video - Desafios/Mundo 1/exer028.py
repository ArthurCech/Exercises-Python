# escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá
# escrever na tela se o usuário venceu ou perde.

from random import randint
from time import sleep

numberComputer = randint(0, 5)

numberUser = int(input('digite um número entre 0 e 5: '))

print('PROCESSANDO...')
sleep(2)

if numberUser == numberComputer:
    print('\033[1;32mVocê acertou! o número era {}\033[m'.format(numberComputer))
else:
    print('\033[1;31mVocê errou! o número era {}\033[m'.format(numberComputer))
