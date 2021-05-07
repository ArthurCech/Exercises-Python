print('exercício 1')

list_numbers = []

for count in range(10):
    number = int(input('digite o {}º número inteiro: '.format(count + 1)))
    list_numbers.append(number)

print('Lista: ')

for number in list_numbers:
    print(number)

print('fim do programa')
