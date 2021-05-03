# a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# até 9 anos: mirim
# até 14 anos: infantil
# até 19 anos: junior
# até 25 anos: sênior
# acima: master

from datetime import date

actualYear = date.today().year

yearOfBirth = int(input('digite o ano de nascimento: '))

age = actualYear - yearOfBirth

if age <= 9:
    print('Idade: {} - Categoria: MIRIM'.format(age))
elif age <= 14:
    print('Idade: {} - Categoria: INFANTIL'.format(age))
elif age <= 19:
    print('Idade: {} - Categoria: JUNIOR'.format(age))
elif age <= 25:
    print('Idade: {} - Categoria: SÊNIOR'.format(age))
else:
    print('Idade: {} - Categoria: MASTER'.format(age))
