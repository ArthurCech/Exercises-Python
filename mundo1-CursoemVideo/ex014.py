# escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

temp_celsius = float(input('digite a temperatura em graus celsius: '))

temp_fahrenheit = (9 * temp_celsius + 160) / 5

print('{:.2f}ºC = {:.2f}ºF'.format(temp_celsius, temp_fahrenheit))
