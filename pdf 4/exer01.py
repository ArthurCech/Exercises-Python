# Escreva um programa que leia um número inteiro e em seguida apresente na tela a tabuada de 0 a 10 para esse número fornecido.:

answerFile = open('exer01.txt', 'w')

number = int(input('digite o número que deseja saber a tabuada: '))

for i in range(11):
    tab = number * i
    print('{} x {} = {}'.format(number, i, tab))
    # print('{} x {} = {}'.format(number, i, tab), file=answerFile)
    answerFile.write('{} x {} = {}\n'.format(number, i, tab))

answerFile.close()