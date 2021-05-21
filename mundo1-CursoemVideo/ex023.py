# faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

number = int(input('digite o número (entre 0 a 9999): '))

uni = number // 1 % 10
ten = number // 10 % 10
hun = number // 100 % 10
tho = number // 1000 % 10

print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(ten))
print('Centena: {}'.format(hun))
print('Milhar: {}'.format(tho))
