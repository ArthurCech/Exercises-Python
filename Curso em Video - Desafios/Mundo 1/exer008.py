# escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

measureMt = float(input('digite a medida em metros: '))

measureCm = measureMt * 100
measureMm = measureMt * 1000

print('{} metros = {} centímetros'.format(measureMt, measureCm))
print('{} metros = {} milímetros'.format(measureMt, measureMm))
