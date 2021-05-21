# faça um programa que leia um número inteiro e diga se ele é ou não um número primo

number = int(input('digite o número (inteiro) que deseja saber se é primo: '))

is_prime = True

for count in range(2, number):
    if number % count == 0:
        is_prime = False

if is_prime:
    print('O número {} é PRIMO!'.format(number))
else:
    print('O número {} não é PRIMO!'.format(number))




# MÉTODO 2
number = int(input('digite o número (inteiro) que deseja saber se é primo: '))
tot = 0

for count in range(1, number + 1):
    if number % count == 0:
        print('\033[33m', end = '')
        tot += 1
    else:
        print('\033[31m', end = '')
    print('{} '.format(count), end = '')
print('\n\033[mO número {} foi divisível {} vezes'.format(number, tot))

if tot == 2:
    print('O número {} é PRIMO!'.format(number))
else:
    print('O número {} não é PRIMO!'.format(number))
