# crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: A) apenas os 5 primeiros colocados; B) os últimos 4 colocados; C) uma lista com os times em ordem alfabética; D) em que posição na tabela está o time da Chapecoense

teams = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
         'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos',
         'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará SC',
         'Vasco da Gama', 'Sport Recife', 'América-MG', 'EC Vitória', 'Paraná')

print(f'Cinco primeiros colocados: {teams[:5]}')
print(f'Últimos quatro colocados: {teams[-4:]}')
print(f'Times em ordem alfabética: {sorted(teams)}')
print(f'Posição da Chapecoense: {teams.index("Chapecoense")}ª colocação')
