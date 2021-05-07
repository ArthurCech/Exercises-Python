print('exercício 6')

answer_file = open('answer_ex06.txt', 'w')

max_value = int(input('digite o limite máximo (inteiro): '))

while max_value < 100:
    max_value = int(input('digite o limite máximo (inteiro): '))

count = 1
sum_even = 0

while count <= max_value:
    if count % 2 == 0:
        sum_even += count
    count += 1

print('Soma dos valores pares que estão entre {} e {} = {}'.format(1, max_value, sum_even))
answer_file.write('Soma dos valores pares que estão entre {} e {} = {}\n'.format(1, max_value, sum_even))

answer_file.close()

print('fim do programa')
