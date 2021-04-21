# Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos e exiba-o na tela um elemento por linha.

listNumbers = []
for i in range(10):
    number = int(input('digite um número inteiro: '))
    listNumbers.append(number)

for number in listNumbers:
    print(number)
