print('Exemplo de Progressão Aritmética')

P = int(input('Digite o primeiro termo: '))
R = int(input('Digite a razão: '))
Q = int(input('Quantidade de elementos: '))

i = 0
soma = 0
while i < Q:
    print('Termo {} da PA = {}'.format(i + 1, P))
    soma += P
    P = P + R
    i += 1

print('Soma dos elementos = {}'.format(soma))

print('Fim do programa')