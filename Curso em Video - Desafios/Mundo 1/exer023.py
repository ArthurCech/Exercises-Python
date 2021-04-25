# faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# ex: 1834
# unidade: 4 - dezena: 3 - centena: 8 - milhar: 1

number = int(input('digite um número de 0 a 9999: '))

unidade = number // 1 % 10
dezena = number // 10 % 10
centena = number // 100 % 10
milhar = number // 1000 % 10

print('\033[1;33munidade: {}\033[m'.format(unidade))
print('\033[1;34mdezena: {}\033[m'.format(dezena))
print('\033[1;35mcentena: {}\033[m'.format(centena))
print('\033[1;36mmilhar: {}\033[m'.format(milhar))
