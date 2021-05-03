# faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas

name = input('digite o nome: ')

print('\033[1;33mSeja bem-vindo, {}!\033[m'.format(name))
