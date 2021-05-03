# faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

number = int(input('digite um número inteiro: '))

u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10

print('\033[1;33mUnidade: \033[1;31m{}\033[m'.format(u))
print('\033[1;33mDezena: \033[1;31m{}\033[m'.format(d))
print('\033[1;33mCentena: \033[1;31m{}\033[m'.format(c))
print('\033[1;33mMilhar: \033[1;31m{}\033[m'.format(m))
