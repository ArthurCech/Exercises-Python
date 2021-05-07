print('exercício 12')

quantity = int(input('digite a quantidade de elementos: '))

while quantity <= 0:
    quantity = int(input('[ERRO] digite a quantidade de elementos: '))

list_numbers = []

for count in range(quantity):
    number = int(input('digite o {}º número inteiro: '.format(count + 1)))
    list_numbers.append(number)

print('Lista: {}'.format(list_numbers))

i = 0
while i < len(list_numbers) - 1:
    j = i + 1
    while j < len(list_numbers):
        if list_numbers[i] == list_numbers[j]:
            del(list_numbers[j])
        else:
            j += 1
    i += 1

print('Lista após remoção dos repetidos: {}'.format(list_numbers))

print('fim do programa')
