# refaça o exercício 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while

first_term = int(input('digite o 1º termo da PA: '))
commom_diff = int(input('digite a razão da PA: '))

count = 0
term = first_term

while count < 10:
    print('{} '.format(term), end = '')
    term += commom_diff
    count += 1
