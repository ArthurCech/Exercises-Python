# Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros gerados aleatoriamente entre 0 e 1000 (usar a função randint da biblioteca random). Exiba na tela a lista gerada. Em seguida, o programa deve ler um valor X e informar se tal valor está, ou não está presente, bem como informar a posição de X na lista. Se houver mais de uma ocorrência de X na lista informe todas as posições.

from random import randint

N = 0
while N <= 0:
    N = int(input('digite a quantidade de elementos: '))

listNumbers = []
for i in range(N):
    listNumbers.append(randint(0, 1000))

print(listNumbers)

X = 0
while X >= 0:
    X = int(input('digite um valor para saber se está na lista: '))
    if X >= 0:
        flag = False
        for i in range(len(listNumbers)):
            if X == listNumbers[i]:
                print('{} está na lista na posição {}'.format(X, i))
                flag = True
        if flag == False:
            print('{} não está na lista'.format(X))
