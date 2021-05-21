# crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

number = int(input('digite o número: '))

double = number * 2
triple = number * 3
square_root = number ** (1 / 2)

print('Dobro de {}: {}'.format(number, double))
print('Triplo de {}: {}'.format(number, triple))
print('Raiz quadrada de {}: {}'.format(number, square_root))
