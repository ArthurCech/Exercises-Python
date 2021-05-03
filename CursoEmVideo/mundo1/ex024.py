# crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cityName = input('digite o nome da cidade: ').strip().upper()

print('\033[1;33mNome da cidade começa com "SANTO"? \033[1;31m{}\033[m'.format(cityName[:5] == 'SANTO'))
