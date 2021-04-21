# Escreva um programa que leia um número N (obrigatoriamente entre 0 e 50) e em seguida leia N números reais em uma lista A. Exiba a lista na tela, um elemento por linha.

qtd = 0
while qtd <= 0 or qtd > 50:
    qtd = int(input('digite a quantidade de valores: '))

listNumbers = []
for i in range(qtd):
    number = float(input('digite um número real: '))
    listNumbers.append(number)

for number in listNumbers:
    print(number)
