# desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
# primeiros termos dessa progressão

firstTerm = int(input('digite o primeiro termo: '))
commonDifference  = int(input('digite a razão: '))
lastTerm = firstTerm + (10 - 1) * commonDifference

for i in range(firstTerm, lastTerm + commonDifference, commonDifference):
    print('{}'.format(i))
