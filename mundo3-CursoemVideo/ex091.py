# crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número do dado

from random import randint
from operator import itemgetter

game = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6),}

print('Valores sorteados:')
for key, value in game.items():
    print(f'{key} obteve {value} no dado')

ranking = dict()
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)

print('Ranking:')
for player, value in enumerate(ranking):
    print(f'{player + 1}º lugar: {value[0]} com {value[1]}')
