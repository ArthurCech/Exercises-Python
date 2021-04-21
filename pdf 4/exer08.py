# Desenvolva um programa que leia do teclado um número inteiro e mostre na tela se esse número é primo ou não. Lembrando: um número primo é divisível somente por 1 e por ele mesmo.

answerFile = open('exer08.txt', 'w')

valor = 2
while valor > 1:
    valor = int(input('digite o valor que deseja saber se é primo: '))

    if valor > 1:
        i = 2
        isPrime = True
        while i < valor:
            if valor % i == 0:
                isPrime = False
            i += 1
            
        if isPrime == True:
            print('{} é um número primo'.format(valor))
            # print('{} é um número primo'.format(valor), file=answerFile)
            answerFile.write('{} é um número primo\n'.format(valor))
        else:
            print('{} não é um número primo'.format(valor))
            # print('{} não é um número primo'.format(valor), file=answerFile)
            answerFile.write('{} não é um número primo\n'.format(valor))

answerFile.close()
