# Escreva um programa que leia dois números quaisquer e mostre 
# na tela qual é o menor e qual é o maior.

A = int(input('digite o valor de A: '))
B = int(input('digite o valor de B: '))

if A > B:
    print('     A ({}) é o maior valor'.format(A))
    print('     B ({}) é o menor valor'.format(B))
elif B > A:
    print('     B ({}) é o maior valor'.format(B))
    print('     A ({}) é o menor valor'.format(A))
else:
    print('     A ({}) e B ({}) são iguais'.format(A, B))
