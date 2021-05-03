# escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

measureMeters = float(input('digite o valor em metros: '))

measureCentimeters = measureMeters * 100
measureMillimeters = measureMeters * 1000

print('\033[1;33m{}m = \033[1;31m{}cm\033[m'.format(measureMeters, measureCentimeters))
print('\033[1;33m{}m = \033[1;31m{}mm\033[m'.format(measureMeters, measureMillimeters))
