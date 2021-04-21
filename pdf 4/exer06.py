# Elaborar um programa que apresente o somatório dos valores pares existentes na faixa entre 1 e N, onde N é um número digitado pelo usuário e que deve ser no mínimo 100 (obrigatório garantir esse requisito).

answerFile = open('exer06.txt', 'w')

N = 1
while N < 100:
    N = int(input('digite a quantidade de elementos: '))

somaPares = 0
i = 1
while i <= N:
    if i % 2 == 0:
        somaPares += i
    i += 1

print('Soma dos valores pares que estão entre {} e {} é {}'.format(1, N, somaPares))
# print('Soma dos valores pares que estão entre {} e {} é {}'.format(1, N, somaPares), file=answerFile)
answerFile.write('Soma dos valores pares que estão entre {} e {} é {}\n'.format(1, N, somaPares))

answerFile.close()

