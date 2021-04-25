# faça um programa que leia um número inteiro e diga se ele é ou não um número primo

number = int(input('digite um número inteiro: '))

# minha solução
isPrime = True
for i in range(2, number):
    if number % i == 0:
        isPrime = False

if isPrime == True:
    print('{} é primo'.format(number))
else:
    print('{} não é primo'.format(number))

# solução Guanabara
tot = 0
for i in range(1, number + 1):
    if number % i == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\033[mO número {} foi divísivel {} vezes'.format(number, tot))

if tot == 2:
    print('É primo')
else:
    print('Não é primo')
