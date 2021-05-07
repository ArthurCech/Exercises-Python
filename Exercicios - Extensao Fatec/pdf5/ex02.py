print('exercício 2')

list_numbers = []
number = 1

while number > 0:
    number = int(input('digite um número inteiro: '))

    if number > 0:
        list_numbers.append(number)

index_number = 0

while index_number < len(list_numbers):
    print(list_numbers[index_number])
    index_number += 1

print('fim do programa')
