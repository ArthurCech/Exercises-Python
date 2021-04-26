# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um 
# triângulo retângulo. Calcule e mostre o comprimento da hipotenusa

from math import hypot

catOposto = float(input('digite o cateto oposto: '))
catAdjacente = float(input('digite o cateto adjacente: '))

# hipotenusa = (catOposto ** 2 + catAdjacente ** 2) ** (1 / 2)
hipotenusa = hypot(catOposto, catAdjacente)

print('\033[1;32mhipotenusa: {}\033[m'.format(hipotenusa))
