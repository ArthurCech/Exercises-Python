# a confederação nacional de natação precisa de um programa que leia o ano de nascimento 
# de um atleta e mostre sua categoria, de acordo com a idade:
# - até 9 anos: mirim
# - até 14 anos: infantil
# - até 19 anos: junior
# - até 20 anos: sênior
# - acima: master

from datetime import date

actualYear = date.today().year

year = int(input('digite o ano de nascimento do atleta: '))

age = actualYear - year

if age <= 9:
    category = 'MIRIM'
elif age <= 14:
    category = 'INFANTIL'
elif age <= 19:
    category = 'JUNIOR'
elif age <= 20:
    category = 'SÊNIOR'
else:
    category = 'MASTER'

print('Idade: {}\nCategoria: {}'.format(age, category))
