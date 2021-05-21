# faça um programa que leia três números e mostre qual é o maior e qual é o menor

number1 = int(input('digite o 1º número: '))
number2 = int(input('digite o 2º número: '))
number3 = int(input('digite o 3º número: '))

biggest = number1

if number2 > number1 and number2 > number3:
    biggest = number2
elif number3 > number1 and number3 > number2:
    biggest = number3

print('Maior valor: {}'.format(biggest))

smallest = number1

if number2 < number1 and number2 < number3:
    smallest = number2
elif number3 < number1 and number3 < number2:
    smallest = number3

print('Menor valor: {}'.format(smallest))
