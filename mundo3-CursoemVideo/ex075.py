# desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) quantas vezes apareceu o valor 9; B) em que posição foi digitado o primeiro valor 3; C) quais foram os números pares

numbers = (int(input('digite o 1º número inteiro: ')),
           int(input('digite o 2º número inteiro: ')),
           int(input('digite o 3º número inteiro: ')),
           int(input('digite o 4º número inteiro: ')),
           int(input('digite o 5º número inteiro: ')))

print('Quantidade de vezes que apareceu o valor 9: {} vezes'.format(numbers.count(9)))

if 3 in numbers:
    print('Primeira vez que apareceu o valor 3: {}'.format(numbers.index(3)))
else:
    print('O 3 não se encontra na tupla')

print('Números pares: ', end = '')
for number in numbers:
    if number % 2 == 0:
        print('{} '.format(number), end = '')
