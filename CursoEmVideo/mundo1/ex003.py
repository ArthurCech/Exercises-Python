# crie um programa que leia dois números e mostre a soma entre elas.

number1 = int(input('digite o 1ª número: '))
number2 = int(input('digite o 2º número: '))

sumNumbers = number1 + number2

print('\033[1;33m{} + {} = {}\033[m'.format(number1, number2, sumNumbers))
