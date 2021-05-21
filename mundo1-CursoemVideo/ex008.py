# escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

value_meters = float(input('digite a medida em metros: '))

value_centimeters = value_meters * 100
value_milimeters = value_meters * 1000

print('{} metros = {} centímetros'.format(value_meters, value_centimeters))
print('{} metros = {} milímetros'.format(value_meters, value_milimeters))
