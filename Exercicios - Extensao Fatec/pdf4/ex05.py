print('exercício 5')

answer_file = open('answer_ex05.txt', 'w')

number = int(input('digite um número inteiro: '))

while number != 0:
    if number % 2 == 0 and number % 3 == 0:
        print('{} é divisível por 2 e por 3'.format(number))
        answer_file.write('{} é divisível por 2 e por 3\n'.format(number))

    number = int(input('digite um número inteiro: '))

answer_file.close()

print('fim do programa')
