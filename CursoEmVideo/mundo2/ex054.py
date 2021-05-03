# crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

from datetime import date

actualYear = date.today().year

sumBelow21 = sumOver21 = 0

for i in range(7):
    yearOfBirth = int(input('digite o ano de nascimento: '))

    age = actualYear - yearOfBirth

    if age < 21:
        sumBelow21 += 1
    else:
        sumOver21 += 1

print('Qtd. de pessoas maiores de 21 anos: {}'.format(sumOver21))
print('Qtd. de pessoas menores de 21 anos: {}'.format(sumBelow21))
