# crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

number = int(input('digite um número inteiro: '))

double = number * 2
triple = number * 3
squareRoot = number ** (1/2)

print('dobro de {} = {}'.format(number, double))
print('triplo de {} = {}'.format(number, triple))
print('raiz quadrada de {} = {:.2f}'.format(number, squareRoot))

# economizar memória
print('dobro de {} = {}'.format(number, number * 2))
print('triplo de {} = {}'.format(number, number * 3))
print('raiz quadrada de {} = {}'.format(number, number ** (1 / 2)))
