# faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto

sex = input('digite o sexo da pessoa [M/F]: ').strip().upper()[0]

while sex != 'M' and sex != 'F': # while sex not int 'MmFf':
    sex = input('[ERRO] digite o sexo da pessoa [M/F] novamente: ').strip().upper()[0]

if sex == 'M':
    print('Sexo masculino')
else:
    sex == 'F'
    print('Sexo feminino')
