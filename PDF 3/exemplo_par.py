print('Exemplo de Par - Ímpar')

X = 1
while X != 0:
    X = int(input('Digite X: '))
    if X % 2 == 0:
        print('{} é par'.format(X))
    else:
        print('{} é ímpar'.format(X))

print('Fim do programa')