# escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

tempCels = float(input('digite a temperatura em graus celsius: '))

tempFahr = (9.0 * tempCels + 160.0) / 5.0

print('\033[1;32m{}ºC = {}ºF\033[m'.format(tempCels, tempFahr))
