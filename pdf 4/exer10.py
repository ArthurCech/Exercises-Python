# Reescreva o programa anterior lendo um número inteiro adicional chamado Prim. Nesta versão o programa deverá apresentar os N termos da sequência de Fibonacci que forem maiores que Prim.

answerFile = open('exer10.txt', 'w')

prim = int(input('digite o valor mínimo a ser mostrado: '))

N = 0
while N <= 0:
    N = int(input('digite a quantidade de termos que deseja visualizar: '))

atual = 0
prox = 1
i = 0
while i < N:
    if atual >= prim:
        print(atual, end=' ')
        # print(atual, end=' ', file=answerFile)
        answerFile.write('{} '.format(atual))
        i += 1
    
    ante = atual
    atual = prox
    prox = ante + atual
    
answerFile.close()

