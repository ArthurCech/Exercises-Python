print('exercício 4')

answer_file = open('answer_ex01.txt', 'w')

number = int(input('digite o número inteiro que deseja saber a tabuada: '))

count = 1

while count < 11:
    mult_value = number * count
    print('{} x {} = {}'.format(number, count, mult_value))
    answer_file.write('{} x {} = {}\n'.format(number, count, number * count))
    count += 1

answer_file.close()

print('fim do programa')
