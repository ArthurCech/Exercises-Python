# Escreva um programa que leia do teclado dois números inteiros nA e nB e leia também duas listas denominados A e B com os tamanhos nA e nB, respectivamente. Na leitura de cada uma das listas é obrigatório que não sejam aceitos valores repetidos. Em seguida, o programa deve juntar as duas listas em um única lista R (resultante) tomando o cuidado de que a lista R não deve ter valores duplicados.

nA = 0
while nA <= 0:
    nA = int(input('digite a quantidade de elementos da lista A: '))

nB = 0
while nB <= 0:
    nB = int(input('digite a quantidade de elementos da lista B: '))

listA = []
for i in range(nA):
    number = int(input('digite um número inteiro para a lista A: '))
    while number in listA:
        number = int(input('digite um número inteiro para a lista A: '))
    listA.append(number)

listB = []
for i in range(nB):
    number = int(input('digite um número inteiro para a lista B: '))
    while number in listB:
        number = int(input('digite um número inteiro para a lista B: '))
    listB.append(number)

listR = listA.copy()
for i in range(len(listB)):
    if listB[i] not in listR:
        listR.append(listB[i])

print(listR)
