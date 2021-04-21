# Escreva um programa que apresente todos os valores inteiros divisíveis por 5 situados entre um valor mínimo e um máximo, fornecidos pelo usuário. É obrigatório que o valor máximo seja maior que o mínimo e se isso não ocorrer, deve ser dada uma mensagem de erro ao usuário.

answerFile = open('exer02.txt', 'w')

minValue = int(input('digite o valor mínimo: '))

maxValue = minValue
while maxValue == minValue:
    maxValue = int(input('digite o valor máximo: '))

if maxValue < minValue:
    minValue, maxValue = maxValue, minValue

i = minValue
while i <= maxValue:
    if i % 5 == 0:
        print('{} é divisível por 5'.format(i))
        # print('{} é divisível por 5'.format(i), file=answerFile)
        answerFile.write('{} é divisível por 5\n'.format(i))
    i += 1

answerFile.close()
