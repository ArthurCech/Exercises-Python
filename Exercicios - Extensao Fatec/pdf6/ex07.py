print('exercício 7')

min_value = int(input('digite o valor mínimo (inteiro): '))
max_value = int(input('digite o valor máximo (inteiro): '))

while min_value == max_value:
    max_value = int(input('[ERRO] digite o valor máximo (inteiro): '))

if min_value > max_value:
    min_value, max_value = max_value, min_value

quantity = int(input('digite a quantidade de elementos: '))

while quantity <= 0:
    quantity = int(input('[ERRO] digite a quantidade de elementos: '))

list_numbers = []

for count in range(quantity):
    number = int(input('digite o {}º número inteiro: '.format(count + 1)))

    if min_value <= number <= max_value:
        list_numbers.append(number)

print('Qtd. de elementos da lista = {}'.format(len(list_numbers)))
print('Lista: {}'.format(list_numbers))

print('fim do programa')
