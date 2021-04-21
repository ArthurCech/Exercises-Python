# Refaça o exercício anterior de modo que os valores inválidos, ou seja, os que estão fora do intervalo [Min, Max] sejam inseridos em uma segunda lista chamada R. Apresentar na tela a lista de valores aceitos (lista A) e a lista de valores rejeitados (lista R), bem como o tamanho de cada um.

LMin = int(input('digite o valor mínimo: '))

LMax = LMin
while LMax == LMin:
    LMax = int(input('digite o valor máximo: '))

if LMax < LMin:
    LMin, LMax = LMax, LMin

N = 0
while N <= 0:
    N = int(input('digite a quantidade de elementos: '))

listNumbersA = []
listNumbersR = []
for i in range(N):
    number = int(input('digite um número inteiro: '))
    if LMin <= number <= LMax:
        listNumbersA.append(number)
    else:
        listNumbersR.append(number)

print('Quantidade de elementos da lista ACEITA: {}'.format(len(listNumbersA)))
print(listNumbersA)
print('Quantidade de elementos da lista REJEITADA: {}'.format(len(listNumbersR)))
print(listNumbersR)
