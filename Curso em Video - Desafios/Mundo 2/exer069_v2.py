# crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos
# B) quantos homens foram cadastrados
# C) quantas mulheres tem menos de 20 anos

tot18 = totH = totM20 = 0
while True:
    age = int(input('digite a idade: '))
    sex = ' '

    while sex not in 'MF':
        sex = input('digite o sexo (M/F): ').strip().upper()
    
    if age >= 18:
        tot18 += 1
    
    if sex == 'M':
        totH += 1
    
    if sex == 'F' and age < 20:
        totM20 += 1
    
    answer = ' '
    while answer not in 'SN':
        answer = input('deseja continuar (S/N): ').strip().upper()
    
    if answer == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens cadastrados: {totH}')
print(f'Total de mulheres com menos de 20 anos: {totM20}')
