# Faça um programa que permaneça em laço até que seja digitado um valor menor ou igual a zero. Cada valor válido (positivo) digitado deve ser inserido em uma lista na posição imediatamente antes do primeiro elemento que seja maior que valor que está sendo inserido. Isso resultará em uma lista ordenada de forma crescente.

listNumbers = []
number = 1
while number > 0:
    number = int(input('digite um número inteiro: '))
    
    i = 0
    while i < len(listNumbers) and number > listNumbers[i]:
        i += 1

    if number > 0:
        listNumbers.insert(i, number)

print(listNumbers)
