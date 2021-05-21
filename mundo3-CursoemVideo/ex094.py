# crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) quantas pessoas foram cadastradas; B) a média de idade do grupo; C) uma lista com todas as mulheres; D) uma lista com todas as pessoas com idade acima da média

people = list()
temp = dict()

sum_age = 0

while True:
    temp['nome'] = input('digite o nome da pessoa: ')

    while True:
        temp['sexo'] = input('digite o sexo da pessoa [M/F]: ').strip().upper()[0]

        if temp['sexo'] in 'MF':
            break

    temp['idade'] = int(input('digite a idade da pessoa: '))

    sum_age += temp['idade']
    
    people.append(temp.copy())
    temp.clear()

    while True:
        enter_person = input('digitar mais uma pessoa [S/N]: ').strip().upper()[0]
        
        if enter_person in 'SN':
            break

    if enter_person == 'N':
        break

average_age = sum_age / len(people)

print(f'Qtd. de pessoas cadastradas: {len(people)}')
print(f'Média de idade do grupo: {average_age:5.2f} anos')
print('Mulheres cadastradas: ', end='')
for person in people:
    print(f'{person["nome"] if person["sexo"] == "F" else ""} ', end='')
print()
print('Pessoas com idade acima da média: ')
for person in people:
    if person['idade'] >= average_age:
        print('      ', end='')

        for key, value in person.items():
            print(f'{key}: {value}; ', end='')
        print()
