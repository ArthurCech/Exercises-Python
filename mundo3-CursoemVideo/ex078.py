# faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

numbers = list()

for count in range(5):
    numbers.append(int(input('digite o {}º número inteiro: '.format(count + 1))))

    if count == 0:
        biggest_number = smallest_number = numbers[count]
    elif numbers[count] > biggest_number:
        biggest_number = numbers[count]
    elif numbers[count] < smallest_number:
        smallest_number = numbers[count]

print(f'Maior valor: {biggest_number} - Índice: ', end='')
for ind, number in enumerate(numbers):
    if number == biggest_number:
        print(f'{ind} ', end='')
print()

print(f'Menor valor: {smallest_number} - Índice: ', end='')
for ind, number in enumerate(numbers):
    if number == smallest_number:
        print(f'{ind} ', end='')
