# faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - se ele ainda vai se alistar ao serviço militar
# - se é a hora de se alistar
# - se já passou do tempo de alistamento
# seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

actualYear = date.today().year

year = int(input('digite o ano de nascimento: '))

age = actualYear - year

if age == 18: 
    print('Hora de se alistar!')
elif age > 18:
    yearsToEnlistment = age - 18
    dateToEnlistment = actualYear - yearsToEnlistment
    print('Você já devia ter se alistado. Passaram {} anos do alistamento'.format(yearsToEnlistment))
    print('Seu alistamento foi em {}'.format(dateToEnlistment))
else: # age < 18
    yearsToEnlistment = 18 - age
    dateToEnlistment = actualYear + yearsToEnlistment
    print('Você não tem 18 anos. Faltam {} anos para se alistar!'.format(yearsToEnlistment))
    print('Seu alistamento será em {}'.format(dateToEnlistment))
