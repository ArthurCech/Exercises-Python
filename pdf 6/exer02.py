# Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos e exiba-o na tela na ordem inversa à ordem de leitura, sendo um elemento por linha da tela.

listNumbers = []
for i in range(10):
    number = int(input('digite um número inteiro: '))
    listNumbers.append(number)

listNumbers.reverse()

for number in listNumbers:
    print(number)
