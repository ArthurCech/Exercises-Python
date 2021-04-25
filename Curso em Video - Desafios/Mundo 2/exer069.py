# crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos
# B) quantos homens foram cadastrados
# C) quantas mulheres tem menos de 20 anos

morePerson = 'S'
qtdAgeOver18 = qtdMen = qtdWomenUnder20 = 0

while morePerson == 'S':
    age = int(input('digite a idade: '))
    sex = input('digite o sexo (M/F) da pessoa: ').strip().upper()

    if age >= 18:
        qtdAgeOver18 += 1
    
    if sex == 'M':
        qtdMen += 1

    if sex == 'F' and age <= 20:
        qtdWomenUnder20 += 1
    print('-' * 25)
    morePerson = input('cadastrar mais pessoas (S/N): ').strip().upper()
    print('-' * 25)

print(f'Quantidade de pessoas acima de 18 anos: {qtdAgeOver18}')
print(f'Quantidade de homens cadastrados: {qtdMen}')
print(f'Quantidade de mulheres com menos de 20 anos: {qtdWomenUnder20}')
