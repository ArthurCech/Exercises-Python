# Faça um programa que leia um número inteiro N obrigatoriamente maior que 10. Preencha uma lista de tamanho N com números inteiros aleatórios. Exiba na tela a lista gerada e em seguida coloque-a em ordem crescente usando o método da bolha. 

from random import randint

N = 0
while N <= 10:
    N = int(input('digite a quantidade de elementos: '))

listNumbers = []
for i in range(N):
    listNumbers.append(randint(0, 1000))

print(listNumbers)

i = 0
while i < len(listNumbers) - 1:
    j = i + 1
    while j < len(listNumbers):
        if listNumbers[i] > listNumbers[j]:
            listNumbers[i], listNumbers[j] = listNumbers[j], listNumbers[i]
        j += 1
    i += 1

print(listNumbers)
