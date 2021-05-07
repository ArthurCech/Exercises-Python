print('exercício 2')

answer_file = open('answer_ex02.txt', 'w')

min_value = int(input('digite o valor mínimo (inteiro): '))
max_value = int(input('digite o valor máximo (inteiro): '))

while max_value == min_value:
    max_value = int(input('digite o valor máximo (inteiro): '))

if min_value > max_value:
    min_value, max_value = max_value, min_value

count = min_value

print('Valores divisíveis por 5 que estão entre {} e {}'.format(min_value, max_value))
answer_file.write('Valores divisíveis por 5 que estão entre {} e {}\n'.format(min_value, max_value))
while count <= max_value:
    if count % 5 == 0:
        print('{}'.format(count), end = ' ')
        answer_file.write('{}  '.format(count))
    count += 1

print()

answer_file.close()

print('fim do programa')
