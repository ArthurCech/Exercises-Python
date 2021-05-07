print('exercício 18')

min_value = int(input('digite o valor mínimo: '))
max_value = int(input('digite o valor máximo: '))

while max_value <= min_value:
    max_value = int(input('[ERRO] digite o valor máximo: '))

list_numbers = []
for count in range(min_value, max_value + 1):
    if count % 7 == 0:
        list_numbers.append(count)

print('Lista: {}'.format(list_numbers))

print('fim do programa')
