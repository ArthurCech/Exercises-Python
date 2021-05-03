# faça um programa que leia um ano qualquer e mostre se ele é bissexto

from datetime import date

year = int(input('digite o ano que deseja saber se é bissexto: '))

if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('\033[1;32mO ano \033[1;36m{} \033[1;32mé bissexto!\033[m'.format(year))
else:
    print('\033[1;31mO ano \033[1;36m{} \033[1;31mnão é bissexto!\033[m'.format(year))
