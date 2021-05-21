# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import hypot

opposite_side = float(input('digite o cateto oposto: '))
adjacent_side = float(input('digite o cateto adjacente: '))

hypotenuse = hypot(opposite_side, adjacent_side)

print('Hipotenusa: {:.2f}'.format(hypotenuse))
