# Escreva um programa que leia um número inteiro e apresente na tela se 
# ele é par ou ímpar (para determinar se um número é par ou ímpar verifique 
# se o resto da divisão dele por 2 é zero ou não. Para isso use o operador % 
# para calcular esse resto).

X = int(input('digite o valor para saber se é par ou ímpar: '))

if X == 0:
    print('     X ({}) é zero'.format(X))
elif X % 2 == 0:
    print('     X ({}) é par'.format(X))
else:
    print('     X ({}) é ímpar'.format(X))
