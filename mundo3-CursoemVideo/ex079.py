# crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numbers = list()

while True:
    number = int(input('digite um número inteiro: '))

    if number not in numbers:
        numbers.append(number)
    else:
        print(f'O número {number} já está na lista')

    enter_number = input('digitar mais um número [S/N]: ').strip().upper()[0]

    if enter_number == 'N':
        break

numbers.sort()

print('Lista: ', end='')
for number in numbers:
    print(f'{number} ', end='')
