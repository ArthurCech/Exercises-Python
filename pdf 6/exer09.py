# Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros gerados aleatoriamente entre 0 e 1000 (usar a função randint da biblioteca random). Exiba na tela a lista gerada. Em seguida, o programa deve ler um valor X e informar se tal valor está, ou não está presente na lista. Neste exercício é permitido usar os operadores in e/ou not in.

from random import randint

N = 0
while N <= 0:
    N = int(input('digite a quantidade de elementos: '))

listNumbers = []
for i in range(N):
    listNumbers.append(randint(0, 1000))

print(listNumbers)

X = 1
while X >= 0:
    X = int(input('digite o valor para verificar se está na lista: '))

    if X in listNumbers:
        print('{} está na lista'.format(X))
    else:
        print('{} não está na lista'.format(X))
