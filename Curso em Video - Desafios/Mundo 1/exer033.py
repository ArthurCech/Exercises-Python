# faça um programa que leia três números e mostre qual é o maior e qual é o menor.

number1 = int(input('digite o 1ª número: '))
number2 = int(input('digite o 2ª número: '))
number3 = int(input('digite o 3ª número: '))

bigger = number1
if number2 > number1 and number2 > number3:
    bigger = number2
elif number3 > number1 and number3 > number2:
    bigger = number3

smaller = number1
if number2 < number1 and number2 < number3:
    smaller = number2
elif number3 < number1 and number3 < number2:
    smaller = number3

print('\033[1;33mO menor número é o {}\033[m'.format(smaller))
print('\033[1;34mO maior número é o {}\033[m'.format(bigger))
