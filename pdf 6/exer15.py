# Escreva um programa que preencha com números inteiros duas listas denominadas A e B com diferentes tamanhos nA e nB, respectivamente. Em seguida o programa deve juntar as duas listas em uma única lista com o tamanho nA+nB. Exibir na tela a lista resultante.

nA = 0
while nA <= 0:
    nA = int(input('digite a quantidade de elementos da lista A: '))

nB = 0
while nB <= 0:
    nB = int(input('digite a quantidade de elementos da lista B: '))

listA = []
for i in range(nA):
    number = int(input('digite um número inteiro para lista A: '))
    listA.append(number)

listB = []
for i in range(nB):
    number = int(input('digite um número inteiro para lista B: '))
    listB.append(number)

listR = listA.copy()
listR.extend(listB)

print(listR)
