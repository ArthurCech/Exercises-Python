# crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for line in range(3):
    for column in range(3):
        matrix[line][column] = int(input(f'digite um valor para [{line}][{column}]: '))

for line in range(3):
    for column in range(3):
        print(f'[{matrix[line][column]:^5}]', end='')
    print()
