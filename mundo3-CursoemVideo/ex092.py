# crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário, se por acaso o CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

from datetime import date

person = dict()

person['nome'] = input('digite o nome: ')
year_birth = int(input('digite o ano de nascimento: '))
person['idade'] = date.today().year - year_birth
person['ctps'] = int(input('digite o número da CTPS (0 para cancelar):'))

if person['ctps'] != 0:
    person['contratacao'] = int(input('digite o ano de contratação: '))
    person['salario'] = float(input('digite o salário: R$ '))
    person['aposentadoria'] = person['idade'] + ((person['contratacao'] + 35) - date.today().year)

for key, value in person.items():
    print(f'{key}: {value}')
