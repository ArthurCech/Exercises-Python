print('exercício 16')

quantity = int(input('digite a quantidade de elementos: '))

while quantity <= 0:
    quantity = int(input('[ERRO] digite a quantidade de elementos: '))

list_numbers = []
count = 0

while count < quantity:
    number = int(input('digite o {}º número inteiro: '.format(count + 1)))

    if number not in list_numbers:
        list_numbers.append(number)
        count += 1
    else:
        print('{} já está na lista'.format(number))

print('Lista final: {}'.format(list_numbers))

print('fim do programa')
