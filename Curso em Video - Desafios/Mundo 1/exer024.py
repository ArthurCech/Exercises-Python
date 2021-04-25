# crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

city = input('digite o nome da cidade que você nasceu: ').strip().lower()

print('\033[1;33mNome da cidade começa com "Santo"?\n{}\033[m'.format(city[:5] == 'santo'))
