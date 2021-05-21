# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: A) a média de idade do grupo; B) qual é o nome do homem mais velho; C) quantas mulheres têm menos de 20 anos.

sum_age = qtd_women_under20 = 0
name_biggest = ''

for count in range(4):
    name = input('digite o nome da {}ª pessoa: '.format(count + 1))
    age = int(input('digite a idade da {}ª pessoa: '.format(count + 1)))
    sex = input('digite o sexo da {}ª pessoa [M/F]: '.format(count + 1)).strip().upper()

    sum_age += age

    if sex == 'M' and name_biggest == '':
        name_biggest = name
        age_biggest = age
    elif sex == 'M' and age > age_biggest:
        name_biggest = name
        age_biggest = age

    if sex == 'F' and age < 20:
        qtd_women_under20 += 1

average_age = sum_age / 4

print('Média das idades: {}'.format(average_age))
print('Homem mais velho: {} - Idade: {}'.format(name_biggest, age_biggest))
print('Qtd. de mulheres com menos de 20 anos: {}'.format(qtd_women_under20))
