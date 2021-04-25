# faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando
# o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final de jogo

from random import randint

wins = 0

while True:
    userNumber = int(input('digite um número inteiro: '))
    computerNumber = randint(0, 11) 
    sumNumbers = userNumber + computerNumber
    userChoice = ' '

    while userChoice  not in 'PI':
        userChoice = input('digite P (par) ou I (ímpar): ').strip().upper()
    
    print(f'Você jogou {userNumber} e o computador {computerNumber}. Total de: {sumNumbers} ', end='')
    print('DEU PAR' if sumNumbers % 2 == 0 else 'DEU ÍMPAR')

    if userChoice == 'P':
        if sumNumbers % 2 == 0:
            print('Você venceu')
            wins += 1
        else:
            print('Você perdeu')
            break
    elif userChoice == 'I':
        if sumNumbers % 2 == 1:
            print('Você venceu')
            wins += 1
        else:
            print('Você perdeu')
            break

print(f'Total de vitórias consecutivas: {wins}')
