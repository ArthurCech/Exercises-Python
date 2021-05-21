# crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome

name = input('digite o nome: ').strip().upper()

print('Nome da pessoa tem SILVA? {}'.format('SILVA' in name))
