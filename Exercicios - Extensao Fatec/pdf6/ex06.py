print('exercício 6')

min_value = int(input('digite o valor mínimo (inteiro): '))
max_value = int(input('digite o valor máximo (inteiro): '))

while min_value == max_value:
    max_value = int(input('[ERRO] digite o valor máximo (inteiro): '))

if min_value > max_value:
    min_value, max_value = max_value, min_value

list_numbers = []

for count in range(10):
    number = int(input('digite o {}º número inteiro: '.format(count + 1)))

    if min_value <= number <= max_value:
        list_numbers.append(number)

print('Qtd. de elementos da lista = {}'.format(len(list_numbers)))
print('Lista: {}'.format(list_numbers))

print('fim do programa')
