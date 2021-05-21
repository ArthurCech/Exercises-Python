# crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas

numbers = list()
odd_numbers = list()
even_numbers = list()

while True:
    numbers.append(int(input('digite um número inteiro: ')))

    enter_number = input('digitar mais um número [S/N]: ').strip().upper()[0]

    if enter_number == 'N':
        break

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print(f'Lista completa: {numbers}')
print(f'Lista pares: {even_numbers}')
print(f'Lista ímpares: {odd_numbers}')
