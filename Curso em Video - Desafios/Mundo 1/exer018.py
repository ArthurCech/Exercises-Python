# faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, 
# cosseno e tangente desse ângulo

from math import radians, sin, cos, tan

angle = float(input('digite o ângulo: '))

seno = sin(radians(angle))
cosseno = cos(radians(angle))
tangente = tan(radians(angle))

print('\033[1;33mSeno: {:.2f}\033[m'.format(seno))
print('\033[1;34mCosseno: {:.2f}\033[m'.format(cosseno))
print('\033[1;35mTangente: {:.2f}\033[m'.format(tangente))
