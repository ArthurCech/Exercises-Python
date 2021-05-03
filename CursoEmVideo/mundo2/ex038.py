# escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# -o primeiro valor é maior
# -o segundo valor é maior
# -não existe valor maior, os dois são iguais

number1 = int(input('digite o 1º número inteiro: '))
number2 = int(input('digite o 2º número inteiro: '))

if number1 > number2:
    print('O 1º valor ({}) é o maior!'.format(number1))
elif number2 > number1:
    print('O 2º valor ({}) é o maior!'.format(number2))
else:
    print('Não existe valor maior, os dois valores são iguais ({}; {})'.format(number1, number2))
