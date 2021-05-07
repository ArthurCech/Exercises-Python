print('exercício 10')

answer_file = open('answer_ex10.txt', 'w')

quantity = int(input('digite a quantidade de termos que deseja visualizar: '))
max_value = int(input('digite o valor máximo para comparação: '))

actual_term = 0
next_term = 1
count = 0

while count < quantity:
    if actual_term >= max_value:
        print('{}'.format(actual_term), end = ' ')
        answer_file.write('{}  '.format(actual_term))
        count += 1
    last_term = actual_term
    actual_term = next_term
    next_term = last_term + actual_term

print()

answer_file.close()

print('fim do programa')
