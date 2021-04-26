# crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

number = int(input('digite o número: '))

if number % 2 == 0:
    print('\033[1;33mO número {} é par\033[m'.format(number))
else:
    print('\033[1;34mO número {} é ímpar\033[m'.format(number))
