# crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar

number = int(input('digite o número inteiro: '))

if number % 2 == 0:
    print('{} é par'.format(number))
else:
    print('{} é ímpar'.format(number))
