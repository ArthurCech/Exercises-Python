# faça um programa que leia três números e mostre qual é o maior e qual é o menor

number1 = int(input('digite o 1ª número: '))
number2 = int(input('digite o 2ª número: '))
number3 = int(input('digite o 3ª número: '))

biggest = number1
if number2 > number1 and number2 > number3:
    biggest = number2
elif number3 > number1 and number3 > number2:
    biggest = number3

smallest = number1
if number2 < number1 and number2 < number3:
    smallest = number2
elif number3 < number1 and number3 < number2:
    smallest = number3

print('\033[1;33mO \033[1;31m{} \033[1;33mé o menor\033[m'.format(smallest))
print('\033[1;33mO \033[1;31m{} \033[1;33mé o maior\033[m'.format(biggest))
