# desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

firstT = int(input('digite o 1º termo da PA: '))
commonDiff = int(input('digite a razão: '))
lastT = firstT + (10 - 1) * commonDiff

for i in range(firstT, lastT + commonDiff, commonDiff):
    print(i)
print('fim do programa')
