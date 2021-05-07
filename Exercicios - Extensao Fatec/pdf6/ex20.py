from random import randint

print('exercício 20')

list_numbers = []

quantity = int(input('digite a quantidade de elementos (maior que 10): '))

while quantity <= 10:
    quantity = int(input('[ERRO] digite a quantidade de elementos (maior que 10): '))

for count in range(quantity):
    number = randint(0, 1000)
    list_numbers.append(number)

print('Lista: {}'.format(list_numbers))

change = True
while change:
    change = False

    i = 0

    while i < len(list_numbers) - 1:
        if list_numbers[i] > list_numbers[i + 1]:
            list_numbers[i], list_numbers[i + 1] = list_numbers[i + 1], list_numbers[i]
            change = True
        i += 1

print('Lista ordenada com bubble sort = {}'.format(list_numbers))

print('fim do programa')
