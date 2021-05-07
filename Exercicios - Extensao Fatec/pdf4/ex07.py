print('exercício 7')

answer_file = open('answer_ex07.txt', 'w')

quantity = sum_numbers = 0

number = int(input('digite um número inteiro: '))

while number > 0:
    if quantity == 0:
        biggest_number = smallest_number = number
    elif number > biggest_number:
        biggest_number = number
    elif number < smallest_number:
        smallest_number = number

    quantity += 1
    sum_numbers += number

    number = int(input('digite um número inteiro: '))

average = sum_numbers / quantity

print('Maior valor = {}'.format(biggest_number))
print('Menor valor = {}'.format(smallest_number))
print('Quantidade de valores = {}'.format(quantity))
print('Soma dos valores = {}'.format(sum_numbers))
print('Média de todos os valores = {}'.format(average))
answer_file.write('Maior valor = {}\n'.format(biggest_number))
answer_file.write('Menor valor = {}\n'.format(smallest_number))
answer_file.write('Quantidade de valores = {}\n'.format(quantity))
answer_file.write('Soma dos valores = {}\n'.format(sum_numbers))
answer_file.write('Média de todos os valores = {}\n'.format(average))

answer_file.close()

print('fim do programa')
