# crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc

number = float(input('digite um número real: '))

print('\033[1;33mNúmero digitado: {} - \033[1;31mNúmero sem casas decimais: {}\033[m'.format(number, trunc(number)))
# usando casting
print('\033[1;33mNúmero digitado: {} - \033[1;31mNúmero sem casas decimais: {}\033[m'.format(number, int(number)))
