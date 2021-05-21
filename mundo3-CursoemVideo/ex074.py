# crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint

numbers = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print('Tupla gerada: ', end = '')
for number in numbers:
    print(f'{number} ', end = '')
print('\nMenor valor: {}'.format(min(numbers)))
print('Maior valor: {}'.format(max(numbers)))
