# faça um programa que leia um número inteiro e diga se ele é ou não um número primo

number = int(input('digite um número inteiro: '))

isPrime = True
for i in range(2, number):
    if number % i == 0:
        isPrime = False

if isPrime:
    print('O número {} é primo'.format(number))
else:
    print('O número {} não é primo'.format(number))



# método guanabara
number = int(input('digite um número inteiro: '))
tot = 0

for i in range(1, number + 1):
    if number % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(i), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(number, tot))

if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
