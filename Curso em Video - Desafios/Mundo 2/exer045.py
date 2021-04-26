# crie um programa que faça o computador jogar jokenpô com você

from random import choice
from time import sleep

userChoice = input('escolha uma opção: pedra | papel | tesoura: ').strip().lower()

computer = ['pedra', 'papel', 'tesoura']
computerChoice = choice(computer)

print('Você jogou {} e o computador jogou {}'.format(userChoice, computerChoice))
print('PROCESSANDO...')
sleep(1)

if userChoice == 'pedra':
    if computerChoice == 'pedra':
        print('EMPATE!')
    elif computerChoice == 'papel':
        print('COMPUTADOR GANHOU!')
    else: # tesoura
        print('VOCÊ GANHOU!')
elif userChoice == 'papel':
    if computerChoice == 'pedra':
        print('VOCÊ GANHOU!')
    elif computerChoice == 'papel':
        print('EMPATE!')
    else: # tesoura
        print('COMPUTADOR GANHOU!')
elif userChoice == 'tesoura':
    if computerChoice == 'pedra':
        print('COMPUTADOR GANHOU!')
    elif computerChoice == 'papel':
        print('VOCÊ GANHOU!')
    else: # tesoura
        print('EMPATE!')
else:
    print('Opção inválida')
