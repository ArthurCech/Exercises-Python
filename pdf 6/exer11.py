# Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros gerados aleatoriamente entre 0 e 1000. Exiba na tela a lista gerada. Em seguida, o programa deve ler um valor X e, caso X esteja na lista, deve eliminá-lo. Caso haja várias ocorrências de X, todas devem ser eliminadas. Pesquise como usar a função del (você vai precisar dela e neste exercício será permitido usá-la).

from random import randint

N = 0
while N <= 0:
    N = int(input('digite a quantidade de elementos: '))

listNumbers = []
for i in range(N):
    listNumbers.append(randint(0, 1000))

print(listNumbers)
print('tamanho original: {}'.format(len(listNumbers)))

X = -1
while X < 0:
    X = int(input('digite o valor que deseja eliminar: '))

i = 0
while i < len(listNumbers):
    if listNumbers[i] == X:
        del(listNumbers[i])
    else:
        i += 1

print(listNumbers)
print('tamanho após as remoções: {}'.format(len(listNumbers)))