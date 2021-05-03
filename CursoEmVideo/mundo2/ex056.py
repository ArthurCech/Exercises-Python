# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# - a média de idade do grupo
# - qual é o nome do homem mais velho
# - quantas mulheres têm menos de 20 anos

sumAge = qtdWomanUnder20 = 0

for i in range(4):
    name = input('digite o nome da {}ª pessoa: '.format(i + 1)).strip()
    age = int(input('digite a idade da {}ª pessoa: '.format(i + 1)))
    sex = input('digite o sexo da {}ª pessoa [M/F]: '.format(i + 1)).strip().upper()

    sumAge += age

    if age < 20 and sex == 'F':
        qtdWomanUnder20 += 1
    if i == 0 and sex == 'M':
        nameOldestMan = name
        ageOldestMan = age
    elif age > ageOldestMan and sex == 'M':
        nameOldestMan = name
        ageOldestMan = age

averageAge = sumAge / 4

print('Média de idade do grupo: {:.2f}'.format(averageAge))
print('Nome do homem mais velho: {} - Idade do homem mais velho: {}'.format(nameOldestMan, ageOldestMan))
print('Qtd. de mulheres abaixo de 20 anos: {}'.format(qtdWomanUnder20))
