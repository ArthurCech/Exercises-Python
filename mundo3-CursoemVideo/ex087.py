# aprimore o desafio anterior, mostrando no final: A) a soma de todos os valores pares digitados; B) a soma dos valores da terceira coluna; C) o maior valor da segunda linha

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for line in range(3):
    for column in range(3):
        matrix[line][column] = int(input(f'digite um valor para [{line}][{column}]: '))

sum_even = sum_third_column = 0

for line in range(3):
    for column in range(3):
        print(f'[{matrix[line][column]:^5}]', end='')
        if matrix[line][column] % 2 == 0:
            sum_even += matrix[line][column]
    print()

for line in range(3):
    sum_third_column += matrix[line][2]

for column in range(3):
    if column == 0:
        biggest_second_line = matrix[1][column]
    elif matrix[1][column] > biggest_second_line:
        biggest_second_line = matrix[1][column]

print(f'Soma de todos os valores: {sum_even}')
print(f'Soma dos valores da 3ª coluna: {sum_third_column}')
print(f'Maior valor da 2ª linha: {biggest_second_line}')
