# crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar

number = int(input('digite um número inteiro: '))

if number % 2 == 0:
    print('\033[1;31m{}\033[1;33m é par\033[m'.format(number))
else:
    print('\033[1;31m{}\033[1;33m é ímpar\033[m'.format(number))
