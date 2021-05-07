print('exercício 9')

answer_file = open('answer_ex09.txt', 'w')

quantity = int(input('digite a quantidade de termos que deseja visualizar: '))

actual_term = 0
next_term = 1
count = 0

while count < quantity:
    print('{}'.format(actual_term), end = ' ')
    answer_file.write('{}  '.format(actual_term))
    last_term = actual_term
    actual_term = next_term
    next_term = last_term + actual_term
    count += 1

print()

answer_file.close()

print('fim do programa')
