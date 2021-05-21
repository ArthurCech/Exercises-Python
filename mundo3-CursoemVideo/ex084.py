# faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A) quantas pessoas foram cadastradas; B) uma listagem com as pessoas mais pesadas; C) uma listagem com as pessoas mais leves

temp = list()
people = list()

while True:
    temp.append(input('digite o nome da pessoa: '))
    temp.append(float(input('digite o peso da pessoa: ')))

    if len(people) == 0:
        biggest_weight = smallest_weight = temp[1]
    elif temp[1] > biggest_weight:
        biggest_weight = temp[1]
    elif temp[1] < smallest_weight:
        smallest_weight = temp[1]

    people.append(temp[:])
    temp.clear()

    enter_person = input('digitar mais uma pessoa [S/N]: ').strip().upper()[0]

    if enter_person == 'N':
        break

print(f'Quantidade de pessoas cadastradas: {len(people)}')
print(f'Pessoas mais pesadas tem {biggest_weight} kg: ', end='')
for person in people:
    if person[1] == biggest_weight:
        print(f'{person[0]} ', end='')
print()
print(f'Pessoas mais leves tem {smallest_weight} kg: ', end='')
for person in people:
    if person[1] == smallest_weight:
        print(f'{person[0]} ', end='')
print()
