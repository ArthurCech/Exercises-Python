# crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos; B) quantos homens foram cadastrados; C)quantas mulheres tem menos de 20 anos

qtd_over18 = qtd_men = qtd_women_under20 = 0

while True:
    age = int(input('digite a idade da pessoa: '))
    sex = input('digite o sexo da pessoa [M/F]: ').strip().upper()[0]

    while sex not in 'MF':
        sex = input('digite o sexo da pessoa [M/F]: ').strip().upper()[0]

    if age >= 18:
        qtd_over18 += 1
    
    if sex == 'M':
        qtd_men += 1

    if sex == 'F' and age < 20:
        qtd_women_under20 += 1

    more_person = input('digite S se deseja continuar ou N se não: ').strip().upper()[0]
    while more_person not in 'SN':
        more_person = input('digite S se deseja continuar ou N se não: ').strip().upper()[0]

    if more_person == 'N':
        break

print('Quantidade de pessoas que tem mais de 18 anos: {}'.format(qtd_over18))
print('Quantidade de homens cadastrados: {}'.format(qtd_men))
print('Quantidade de mulheres com menos de 20 anos: {}'.format(qtd_women_under20))
