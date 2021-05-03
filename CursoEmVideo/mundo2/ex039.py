# faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# -se ele ainda vai se alistar ao serviço militar
# -se é a hora de se alistar
# -se já passou do tempo de alistamento
# seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

actualYear = date.today().year

yearOfBirth = int(input('digite o ano de nascimento: '))

age = actualYear - yearOfBirth

if age == 18:
    print('Você tem {} anos.'.format(age))
    print('É hora de se alistar!')
elif age < 18:
    qtdYears = 18 - age
    yearToJoin = actualYear + qtdYears
    print('Você tem {} anos.'.format(age))
    print('Faltam {} anos para o alistamento.'.format(qtdYears))
    print('Ano do alistamento: {}'.format(yearToJoin))
else:
    qtdYears = age - 18
    yearToJoin = actualYear - qtdYears
    print('Você tem {} anos.'.format(age))
    print('Passaram {} anos do alistamento.'.format(qtdYears))
    print('Ano do alistamento: {}'.format(yearToJoin))
