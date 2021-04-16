print('Exercício 01 do PDF Parte 4')

fileAnswer = open('exer01.txt', 'w')

num = int(input('Digite o número para saber a tabuada: '))

for i in range(11): # 0 a 10
    tab = num * i
    print('{} x {} = {}'.format(num, i, tab))
    print('{} x {} = {}'.format(num, i, tab), file=fileAnswer)

fileAnswer.close()

print('Fim do programa')