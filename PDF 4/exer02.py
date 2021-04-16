print('Exercício 02 do PDF Parte 4')

fileAnswer = open('exer02.txt', 'w')

minValue = int(input('Digite o valor mínimo: '))

maxValue = minValue
while maxValue == minValue:
    maxValue = int(input('Digite o valor máximo: '))

if minValue > maxValue:
    minValue, maxValue = maxValue, minValue

i = minValue
while i <= maxValue:
    if i % 5 == 0:
        print('{} é divisível por 5'.format(i))
        print('{} eh divisivel por 5'.format(i), file=fileAnswer)
    i += 1

fileAnswer.close()

print('Fim do programa')