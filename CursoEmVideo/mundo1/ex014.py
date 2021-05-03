# escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

temperatureCelsius = float(input('digite a temperatura em graus celsius: '))

temperatureFahrenheit = (9 * temperatureCelsius + 160) / 5

print('\033[1;33m{:.2f}ºC = \033[1;31m{:.2f}ºF\033[m'.format(temperatureCelsius, temperatureFahrenheit))
