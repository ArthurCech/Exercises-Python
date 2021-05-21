# faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

from random import randint

qtd_games = int(input('digite a quantidade de jogos que serão gerados: '))

games = list()
temp = list()

for count_games in range(qtd_games):
    for count_numbers in range(6):
        number = randint(1, 60)
        
        while number in temp:
            number = randint(1, 60)

        temp.append(number)

    temp.sort()
    games.append(temp[:])
    temp.clear()

print('Jogos gerados:')
for index, game in enumerate(games):
    print(f'Jogo {index + 1}: {game}')




# MÉTODO 2
from random import randint

qtd_games = int(input('digite a quantidade de jogos que serão gerados: '))

games = list()
temp = list()

tot = 1
while tot <= qtd_games:
    cont = 0
    while True:
        number = randint(1, 60)
        
        if number not in temp:
            temp.append(number)
            cont += 1
        if cont >= 6:
            break

    temp.sort()
    games.append(temp[:])
    temp.clear()
    tot += 1

print('Jogos gerados:')
for index, game in enumerate(games):
    print(f'Jogo {index + 1}: {game}')
