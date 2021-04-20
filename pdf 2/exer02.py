# Escreva um programa que leia dois números inteiros A e B e 
# mostre na tela apenas o menor dos dois.

A = int(input('digite o valor de A: '))
B = int(input('digite o valor de B: '))

print('O menor valor é: ')
if A < B:
    print('     A = {}'.format(A))
elif B < A:
    print('     B = {}'.format(B))
else:
    print('     A ({}) e B ({}) são iguais'.format(A, B))
