print('exercício 8')

answer_file = open('answer_ex08.txt', 'w')

number = int(input('digite o número (inteiro) para saber se é primo: '))

is_prime = True
count = 2

while count < number:
    if number % count == 0:
        is_prime = False

    count += 1

if is_prime:
    print('{} é um número primo'.format(number))
    answer_file.write('{} é um número primo\n'.format(number))
else:
    print('{} não é um número primo'.format(number))
    answer_file.write('{} não é um número primo\n'.format(number))

answer_file.close()

print('fim do programa')
