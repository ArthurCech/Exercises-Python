# escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma 
# mensagem:
# - o primeiro valor é maior
# - o segundo valor é maior
# - não existe valor maior, os dois são iguais

number1 = int(input('digite o 1º número inteiro: '))
number2 = int(input('digite o 2º número inteiro: '))

if number1 > number2:
    print('O primeiro valor ({}) é maior'.format(number1))
elif number2 > number1:
    print('O segundo valor ({}) é maior'.format(number2))
else:
    print('Os números são iguais (Num1: {} e Num2: {}).'.format(number1, number2))
