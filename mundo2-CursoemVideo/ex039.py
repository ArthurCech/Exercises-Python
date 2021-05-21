# faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo de alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

current_year = date.today().year
year_birth = int(input('digite o ano de nascimento: '))

age = current_year - year_birth

if age > 18:
    qtd_years = age - 18
    year_join = current_year - qtd_years
    print('Você se alistou em {}'.format(year_join))
    print('Passaram {} anos do alistamento'.format(qtd_years))
elif age < 18:
    qtd_years = 18 - age
    year_join = current_year + qtd_years
    print('Você vai se alistar em {}'.format(year_join))
    print('Faltam {} anos para se alistar'.format(qtd_years))
else:
    print('Você deve se alistar este ano ({})'.format(current_year))
