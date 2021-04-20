# Escreva um programa que leia um número inteiro N e em seguida leia N 
# números reais, separando o menor e o maior, apresentando-os na tela.

answerFile = open('exer03.txt', 'w')

N = int(input('digite a quantidade de elementos: '))

i = 0
while i < N:
    valor = float(input('digite um número real: '))

    if i == 0:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor

    i += 1

print('maior valor = {}'.format(maior))
print('menor valor = {}'.format(menor))

print('maior valor = {}'.format(maior), file=answerFile)
print('menor valor = {}'.format(menor), file=answerFile)

answerFile.close()

