# Escreva um programa que leia um número inteiro N e em seguida leia N 
# números reais, calculando a soma de todos os valores digitados.

N = int(input('digite a quantidade de elementos: '))

i = 0
soma = 0.0
while i < N:
    X = float(input('digite um número real: '))
    soma += X
    i += 1

print('Soma dos valores digitados = {}'.format(soma))
