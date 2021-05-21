# escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: o primeiro valor é maior, o segundo valor é maior, não existe valor maior, os dois são iguais

number1 = int(input('digite o 1º número inteiro: '))
number2 = int(input('digite o 2º número inteiro: '))

if number1 > number2:
    print(f'o primeiro valor ({number1}) é maior')
elif number2 > number1:
    print(f'o segundo valor ({number2}) é maior')
else:
    print('os números são iguais')
