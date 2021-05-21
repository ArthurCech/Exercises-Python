# desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

first_term = int(input('digite o 1º termo da PA: '))
commom_diff = int(input('digite a razão da PA: '))
last_term = first_term + (10 - 1) * commom_diff

for term in range(first_term, last_term + commom_diff, commom_diff):
    print('{} '.format(term), end = '')
