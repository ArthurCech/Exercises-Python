# melhore o exercício 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos

first_term = int(input('digite o 1º termo da PA: '))
commom_diff = int(input('digite a razão da PA: '))

count = 0
tot_numbers = 0
more_terms = 10
term = first_term

while more_terms > 0:
    tot_numbers += more_terms
    while count < tot_numbers:
        print('{} '.format(term), end = '')
        term += commom_diff
        count += 1

    more_terms = int(input('\ndigite a quantidade de termos que quer mostrar a mais: '))
