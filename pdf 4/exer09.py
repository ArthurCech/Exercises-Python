# Escreva um programa que leia um número inteiro N e em seguida apresente na tela os N primeiros termos da sequência de Fibonacci. Essa sequência tem como regra de formação o fato de um número ser a soma dos dois anteriores, sendo que os dois primeiros termos da sequência são, respectivamente, 0 e 1.

answerFile = open('exer09.txt', 'w')

N = 0
while N <= 0:
    N = int(input('digite a quantidade de termos que deseja visualizar: '))

atual = 0
prox = 1
i = 0
while i < N:
    print(atual, end=' ')
    # print(atual, end=' ', file=answerFile)
    answerFile.write('{} '.format(atual))
    ante = atual
    atual = prox
    prox = ante + atual
    i += 1

answerFile.close()
