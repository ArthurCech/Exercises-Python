print('Exercício 01 do PDF Parte 3')

P = int(input('Digite o primeiro termo: '))
R = int(input('Digite a razão: '))
N = int(input('Digite a quantidade de elementos: '))

soma = 0
i = 0
while i < N:
    print(P, end=' ')
    soma += P
    P *= R
    i += 1

print('\nSoma dos elementos = {}'.format(soma))

print('Fim do programa')