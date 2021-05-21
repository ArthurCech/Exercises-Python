# crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato

player = dict()
goals = list()

player['nome'] = input('digite o nome do jogador: ')
player['jogos'] = int(input('digite a quantidade de jogos que o jogador jogou: '))

for games in range(player['jogos']):
    goals.append(int(input(f'digite a qtd. de gols marcados na {games + 1}ª partida: ')))

player['gols-partida'] = goals.copy()
player['total-gols'] = sum(goals)

print('-' * 30)

for key, value in player.items():
    print(f'{key}: {value}')

print('-' * 30)

print(f'O jogador {player["nome"]} jogou {len(player["gols-partida"])} partidas')
for match, value in enumerate(player['gols-partida']):
    print(f'    => Partida {match} = {value} gols')

print(f'Total de gols feitos: {player["total-gols"]}')
