# crie um programa que faça o computador jogar jonkepô com você

from random import randint

options = ['pedra', 'papel', 'tesoura']

print('''OPÇÕES:
( 0 ) - pedra
( 1 ) - papel
( 2 ) - tesoura''')

user_option = int(input('digite uma opção: '))

computer_option = randint(0, 2)

print('JOGADOR: {}'.format(options[user_option]))
print('COMPUTADOR: {}'.format(options[computer_option]))

if user_option == 1: # pedra
    if computer_option == 1:
        print('EMPATE')
    elif computer_option == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADOR VENCEU')
elif user_option == 2: # papel
    if computer_option == 2:
        print('EMPATE')
    elif computer_option == 1:
        print('JOGADOR VENCEU')
    else:
        print('COMPUTADOR VENCEU')
elif user_option == 3: # tesoura
    if computer_option == 3:
        print('EMPATE')
    elif computer_option == 1:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADOR VENCEU')
else:
    print('Opção inválida')




# MÉTODO 2

from random import choice

options = ['pedra', 'papel', 'tesoura']

user_option = input('digite uma opção (pedra | papel | tesoura): ').strip().lower()

computer_option = choice(options)

print('JOGADOR: {}'.format(user_option))
print('COMPUTADOR: {}'.format(computer_option))

if user_option == 'pedra': # pedra
    if computer_option == 'pedra':
        print('EMPATE')
    elif computer_option == 'papel':
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADOR VENCEU')
elif user_option == 'papel': # papel
    if computer_option == 'papel':
        print('EMPATE')
    elif computer_option == 'pedra':
        print('JOGADOR VENCEU')
    else:
        print('COMPUTADOR VENCEU')
elif user_option == 'tesoura': # tesoura
    if computer_option == 'tesoura':
        print('EMPATE')
    elif computer_option == 'pedra':
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADOR VENCEU')
else:
    print('Opção inválida')
