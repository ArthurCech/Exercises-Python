# faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import radians, sin, cos, tan

angle = float(input('digite o ângulo: '))

sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))

print('Seno de {}º: {:.2f}'.format(angle, sine))
print('Cosseno de {}º: {:.2f}'.format(angle, cosine))
print('Tangente de {}º: {:.2f}'.format(angle, tangent))
