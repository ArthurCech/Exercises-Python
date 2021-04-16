print('Exercício 06 do PDF Parte 4')

fileAnswer = open('exer06.txt', 'w')

minValue = 1
while minValue < 100:
    minValue = int(input('Digite o valor mínimo: '))

i = 1
somaPar = 0
while i <= minValue:
    if i % 2 == 0:
        somaPar += i
    i += 1

print('Soma dos pares entre {} e {} = {}'.format(1, minValue, somaPar))
print('Soma dos pares entre {} e {} = {}'.format(1, minValue, somaPar), file=fileAnswer)

fileAnswer.close()

print('Fim do programa')