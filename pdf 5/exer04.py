# Escreva um programa que leia do teclado duas listas com tamanho 10, com números inteiros. Em seguida o programa deve juntar as duas listas em uma única com o tamanho 20.

listNumbers1 = []
for i in range(10):
    number = int(input('digite um número inteiro para lista 1: '))
    listNumbers1.append(number)

listNumbers2 = []
for i in range(10):
    number = int(input('digite um número inteiro para lista 2: '))
    listNumbers2.append(number)

finalList = listNumbers1.copy() # finalList = listNumbers1[:]
finalList.extend(listNumbers2)

print(finalList)
