# Escreva um programa que leia um número inteiro N e em seguida leia N 
# números reais, calculando a soma de todos os valores positivos 
# fornecidos, ignorando os negativos.

N = int(input('digite a quantidade de elementos: '))

i = 0
somaPositivos = 0.0
while i < N:
    X = float(input('digite um número real: '))
    if i >= 0:
        somaPositivos += X
    i += 1

print('Soma dos valores positivos = {}'.format(somaPositivos))
