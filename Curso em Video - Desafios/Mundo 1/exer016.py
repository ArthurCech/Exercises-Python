# crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua 
# porção inteira

from math import trunc

number = float(input('digite um número real: '))

print('\033[1;33mnúmero inteiro - trunc: {}\033[m'.format(trunc(number)))
print('\033[1;34mnúmero inteiro - função interna: {}\033[m'.format(int(number)))
