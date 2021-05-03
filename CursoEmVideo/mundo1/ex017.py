# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import hypot

oppositeLeg = float(input('digite o valor do cateto oposto: '))
adjacentLeg = float(input('digite o valor do cateto adjacente: '))

hypotenuse = hypot(oppositeLeg, adjacentLeg)

print('\033[1;33mHipotenusa: \033[1;31m{:.2f}\033[m'.format(hypotenuse))
