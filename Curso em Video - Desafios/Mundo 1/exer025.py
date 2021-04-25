# crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

name = input('digite o nome da pessoa: ').strip().lower()

hasSilva = 'silva' in name

print('\033[1;33mO nome tem "silva"? {}\033[m'.format(hasSilva))
