# refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while

firstT = int(input('digite o 1º termo da PA: '))
commonDiff  = int(input('digite a razão: '))

i = 0
term = firstT
while i < 10:
    print('{}'.format(term), end=' ')
    term += commonDiff
    i += 1
