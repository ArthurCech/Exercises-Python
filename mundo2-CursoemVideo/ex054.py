# crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

from datetime import date

current_year = date.today().year

qtd_older = qtd_minor = 0

for count in range(7):
    year_birth = int(input('digite o ano de nascimento da {}ª pessoa: '.format(count + 1)))
    age = current_year - year_birth

    if age >= 21:
        qtd_older += 1
    else:
        qtd_minor += 1

print('{} pessoas atingiram a maioridade'.format(qtd_older))
print('{} pessoas não atingiram a maioridade'.format(qtd_minor))
