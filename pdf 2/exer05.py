# Escreva um programa que leia um número inteiro e informe 
# se o mesmo é positivo, zero ou negativo.

X = int(input('digite o valor de X: '))

if X == 0:
    print('     X ({}) é zero'.format(X))
elif X > 0:
    print('     X ({}) é positivo'.format(X))
else:
    print('     X ({}) é negativo'.format(X))
