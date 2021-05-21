# crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições

from datetime import date

def voto(year_birth):
    current_year = date.today().year
    age = current_year - year_birth

    if age >= 18:
        return f'Idade: {age} anos - Situação: VOTO OBRIGATÓRIO'
    elif age >= 16:
        return f'Idade: {age} anos - Situação: VOTO OPCIONAL'
    else:
        return f'Idade: {age} anos - Situação: VOTO NEGADO'


year_birth = int(input('digite o ano de nascimento: '))
print(f'{voto(year_birth)}')
