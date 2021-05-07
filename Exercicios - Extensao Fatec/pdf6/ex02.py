print('exercício 2')

list_numbers = []

for count in range(10):
    number = int(input('digite o {}º número inteiro: '.format(count + 1)))
    list_numbers.append(number)

list_numbers.reverse()

print('Lista:')

for number in list_numbers:
    print(number)

print('fim do programa')
