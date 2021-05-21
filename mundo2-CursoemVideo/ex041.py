# a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: até 9 anos - mirim; até 14 anos - infantil; até 19 anos - junior; até 25 anos - sênior; acima - master

from datetime import date

current_year = date.today().year
year_birth = int(input('digite o ano de nascimento do atleta: '))

age = current_year - year_birth

if age <= 9:
    category = 'Mirim'
elif age <= 14:
    category = 'Infantil'
elif age <= 19:
    category = 'Junior'
elif age <= 25:
    category = 'Sênior'
else:
    category = 'Master'

print('{} anos se enquadra na categoria {}'.format(age, category))
