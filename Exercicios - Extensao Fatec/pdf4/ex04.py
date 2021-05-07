print('exercício 4')

answer_file = open('answer_ex04.txt', 'w')

quantity = int(input('digite a quantidade de números reais: '))

count = 0

while count < quantity:
    number = float(input('digite um número real: '))

    if number > 0:
        if count == 0:
            biggest_number = smallest_number = number
        elif number > biggest_number:
            biggest_number = number
        elif number < smallest_number:
            smallest_number = number
        
        count += 1
    else:
        print('[ERRO] número inválido')

print('Maior valor digitado: {}'.format(biggest_number))
print('Menor valor digitado: {}'.format(smallest_number))
answer_file.write('Maior valor digitado: {}\n'.format(biggest_number))
answer_file.write('Menor valor digitado: {}\n'.format(smallest_number))

answer_file.close()

print('fim do programa')
