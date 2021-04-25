# crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

print('Números pares: ', end='')
for i in range(1, 51):
    if i % 2 == 0:
        print('{} '.format(i), end='')
