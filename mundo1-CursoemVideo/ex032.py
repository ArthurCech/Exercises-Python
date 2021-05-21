# faça um programa que leia um ano qualquer e mostre se ele é bissexto

year = int(input('digite o ano: '))

if year % 4 == 0 and year % 100 != 0  or year % 400 == 0:
    print('O ano {} é bissexto'.format(year))
else:
    print('O ano {} não é bissexto'.format(year))
