# Escreva um programa que contenha um laço que será executado enquanto o número digitado for diferente de zero. Para cada número digitado pelo usuário mostrar na tela apenas os que forem divisíveis por 2 e por 3.

answerFile = open('exer05.txt', 'w')

X = 1
while X != 0:
    X = int(input('digite o valor: '))

    if X != 0:
        if X % 2 == 0 and X % 3 == 0:
            print('{} é divisível por 2 e por 3'.format(X))
            # print('{} é divisível por 2 e por 3'.format(X), file=answerFile)
            answerFile.write('{} é divisível por 2 e por 3\n'.format(X))

answerFile.close()
