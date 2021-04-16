# números primos: maior que 1, divisíveis por 1 e por ele mesmo

def primeNumber(value):
    i = 2
    while i < value:
        if value % i == 0:
            return False
        i += 1
    return True

print('Exercício 08 do PDF Parte 4')

fileAnswer = open('exer08.txt', 'w')

num = 1
while num < 2:
    num = int(input('Digite o valor para saber se é primo: '))

if primeNumber(num):
    print('{} é primo!'.format(num))
    print('{} é primo!'.format(num), file=fileAnswer)
else:
    print('{} não é primo!'.format(num))
    print('{} nao eh primo!'.format(num), file=fileAnswer)

fileAnswer.close()

print('Fim do programa')