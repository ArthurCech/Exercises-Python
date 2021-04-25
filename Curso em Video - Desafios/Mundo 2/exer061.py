# refaça o exer051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
# da progressão usando a estrutura while

firstTerm = int(input('digite o primeiro termo: '))
commonDifference  = int(input('digite a razão: '))

i = 0
term = firstTerm
while i < 10:
    print('{}'.format(term), end=' ')
    term += commonDifference
    i += 1
