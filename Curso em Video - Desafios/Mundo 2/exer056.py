# desenvolva um programa que leia o nome, a idade e o sexo de 4 pessoas. No final do programa mostre:
# - a média de idade do grupo
# - qual é o nome do homem mais velho
# - quantas mulheres têm menos de 20 anos

sumAge = 0
sumWomenUnder20 = 0

for i in range(4):
    print('------------{} PESSOA------------'.format(i + 1))
    name = input('digite o nome da pessoa {}: '.format(i + 1)).strip()
    age = int(input('digite a idade da pessoa {}: '.format(i + 1))).strip()
    sex = input('digite o sexo (M/F) da pessoa {}: '.format(i + 1)).strip().lower()

    sumAge += age

    if sex == 'm' and i == 0:
        ageOldestMan = age
        nameOldestMan = name
    elif sex == 'm' and ageOldestMan < age:
        ageOldestMan = age
        nameOldestMan = name
    elif sex == 'f' and age < 20:
        sumWomenUnder20 += 1
    

averageAge = sumAge / 4

print('Média de idade do grupo: {}'.format(averageAge))
print('Nome do homem mais velho: {}'.format(nameOldestMan))
print('Idade do homem mais velho: {}'.format(ageOldestMan))
print('Qtd. de mulheres com menos de 20 anos: {}'.format(sumWomenUnder20))
