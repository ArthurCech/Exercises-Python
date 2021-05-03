# crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome

name = input('digite o nome da pessoa: ').strip().upper()

print('\033[1;33mO nome da pessoa tem "SILVA"? \033[1;31m{}\033[m'.format('SILVA' in name))
