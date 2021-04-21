# Escreva um programa que leia do teclado duas listas com tamanho 10, com números inteiros. Em seguida o programa deve juntar as duas listas em uma única lista com o tamanho 20.

listA = []
for i in range(10):
    number = int(input('digite um número inteiro para lista A: '))
    listA.append(number)

listB = []
for i in range(10):
    number = int(input('digite um número inteiro para lista B: '))
    listB.append(number)

finalList = listA.copy()
finalList.extend(listB)

print(finalList)
