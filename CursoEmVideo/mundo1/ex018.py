# faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente dessê angulo.

from math import radians, sin, cos, tan

angleValue = float(input('digite o ângulo: '))

sinValue = sin(radians(angleValue))
cosValue = cos(radians(angleValue))
tanValue = tan(radians(angleValue))

print('\033[1;33mSeno: \033[1;31m{:.2f}\033[m'.format(sinValue))
print('\033[1;33mCosseno: \033[1;31m{:.2f}\033[m'.format(cosValue))
print('\033[1;33mTangente: \033[1;31m{:.2f}\033[m'.format(tanValue))
