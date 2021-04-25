# faça um programa que leia um ano qualquer e mostre se ele é bissexto

# from datetime import date

# year = date.today().year

year = int(input('digite o ano para saber se é bissexto: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('\033[1;32mO ano {} é bissexto\033[m'.format(year))
else:
    print('\033[1;31mO ano {} não é bissexto\033[m'.format(year))
