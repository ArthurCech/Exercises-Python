# faça um programa que tenha uma função chamada ficha() que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente

def ficha(name_player='unknown', qtd_goals=0):
    print(f'O jogador {name_player} fez {qtd_goals} gol(s)')


name_player = input('digite o nome do jogador: ')
qtd_goals = input('digite a quantidade de gols: ')

if qtd_goals.isnumeric():
    qtd_goals = int(qtd_goals)
else:
    qtd_goals = 0

if name_player.strip() == '':
    ficha(qtd_goals=qtd_goals)
else:
    ficha(name_player, qtd_goals)
