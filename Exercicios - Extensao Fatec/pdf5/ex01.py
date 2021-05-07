print('exercício 1')

list_numbers = []
number = 1

while number > 0:
    number = int(input('digite um número inteiro: '))

    if number > 0:
        list_numbers.append(number)

print('Lista criada = {}'.format(list_numbers))

# iterando com for
print('Lista criada:')

for number in list_numbers:
    print(number)

print('fim do programa')
