# crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc

number = float(input('digite o número real: '))

print('Porção inteira do número digitado: {}'.format(trunc(number)))
# utilizando casting
print('Porção inteira do número digitado: {}'.format(int(number)))
