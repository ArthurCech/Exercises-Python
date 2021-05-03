# crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

number = int(input('digite um número inteiro: '))

double = number * 2
triple = number * 3
squareRoot = number ** (1 / 2)

print('\033[1;33mDobro de {}: \033[1;31m{}\033[m'.format(number, double))
print('\033[1;33mTriplo de {}: \033[1;31m{}\033[m'.format(number, triple))
print('\033[1;33mRaiz quadrada de \033[1;31m{}: {:.2f}\033[m'.format(number, squareRoot))
