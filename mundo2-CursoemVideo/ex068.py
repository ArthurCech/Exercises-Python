# faça um programa que jogue par ou ímpar com o computador. O jogo só sera interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint

victories = 0

while True:
    computer_number = randint(0, 10)
    user_number = int(input('digite um número entre 0 e 10: '))
    sum_numbers = computer_number + user_number

    option = ' '
    while option not in 'PI':
        option = input('digite a opção [P-par/I-ímpar]: ').strip().upper()[0]
    
    print('Jogador: {}'.format(user_number))
    print('Computador: {}'.format(computer_number))
    print('Total: {}'.format(sum_numbers))

    if option == 'P':
        if sum_numbers % 2 == 0:
            print('Jogador venceu')
            victories += 1
        else:
            print('Jogador perdeu')
            break
    else:
        if sum_numbers % 2 != 0:
            print('Jogador venceu')
            victories += 1
        else:
            print('Jogador perdeu')
            break

print('Jogador venceu {} vezes'.format(victories))
