# crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

city_name = input('digite o nome da cidade: ').strip().upper()

print('Nome da cidade começa com SANTO? {}'.format(city_name[:5] == 'SANTO'))
