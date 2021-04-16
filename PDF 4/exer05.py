print('Exercício 05 do PDF Parte 4')

fileAnswer = open('exer05.txt', 'w')

num = 1
while num != 0:
    num = int(input('Digite um número inteiro: '))
    if num != 0:
        if num % 2 == 0 and num % 3 == 0:
            print('{} é divisível por 2 e 3'.format(num))
            print('{} eh divisivel por 2 e 3'.format(num), file=fileAnswer)

fileAnswer.close()

print('Fim do programa')