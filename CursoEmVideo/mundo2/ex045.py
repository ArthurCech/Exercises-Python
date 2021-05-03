# crie um programa que faça o computador jogar jokenpô com você

from random import choice
from time import sleep

choices = ['pedra', 'papel', 'tesoura']

user = input('digite uma opção: pedra|papel|tesoura: ').strip().lower()
computer = choice(choices)

print('PROCESSANDO...')
sleep(2)

print('Você jogou: {}'.format(user))
print('Computador jogou: {}'.format(computer))

if user == 'pedra':
    if computer == 'pedra':
        print('\033[1;33mEMPATE\033[m')
    elif computer == 'papel':
        print('\033[1;31mCOMPUTADOR GANHOU\033[m')
    else: # tesoura
        print('\033[1;32mJOGADOR GANHOU\033[m')
elif user == 'papel':
    if computer == 'papel':
        print('\033[1;33mEMPATE\033[m')
    elif computer == 'pedra':
        print('\033[1;32mJOGADOR GANHOU\033[m')
    else: # tesoura
        print('\033[1;31mCOMPUTADOR GANHOU\033[m')
elif user == 'tesoura':
    if computer == 'tesoura':
        print('\033[1;33mEMPATE\033[m')
    elif computer == 'pedra':
        print('\033[1;31mCOMPUTADOR GANHOU\033[m')
    else:
        print('\033[1;32mJOGADOR GANHOU\033[m')
else:
    print('Opção inválida!')
