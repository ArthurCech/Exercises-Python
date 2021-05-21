# aprimore o exercício 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador

temp_player = dict() # armazenar um jogador
players = list() # armazenar todos os jogadores
goals = list() # armazenar os gols

while True:
    temp_player.clear()

    temp_player['nome'] = input('digite o nome do jogador: ')
    temp_player['jogos'] = int(input('digite a quantidade de jogos que o jogador jogou: '))
    
    goals.clear()

    for games in range(temp_player['jogos']):
        goals.append(int(input(f'digite a qtd. de gols marcados na {games + 1}ª partida: ')))

    temp_player['gols-partida'] = goals.copy()
    temp_player['total-gols'] = sum(goals)

    players.append(temp_player.copy())

    while True:
        enter_person = input('digitar mais uma pessoa [S/N]: ').strip().upper()[0]
        
        if enter_person in 'SN':
            break

    if enter_person == 'N':
        break

print('-=' * 30)

print('cod ', end='')

for key in temp_player.keys():
    print(f'{key:<15}', end='')
print()

print('-' * 40)

for index, value in enumerate(players):
    print(f'{index:>3} ', end='')

    for d in value.values():
        print(f'{str(d):<15}', end='')

    print()

print('-' * 40)

while True:
    search = int(input('digite o número do jogador (999 para cancelar): '))

    if search == 999:
        break
    if search >= len(players):
        print(f'[ERRO] não existe jogador com esse número')
    else:
        print(f'JOGADOR: {players[search]["nome"]}')

        for index, goal in enumerate(players[search]['gols-partida']):
            print(f'    Jogo {index + 1}: {goal} gols')
        
        print('-' * 40)
