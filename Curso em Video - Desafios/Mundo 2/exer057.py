# faça um programa que leia o sexo de uma pessoa, mas só aceite os valores'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto

sex = input('digite o sexo da pessoa (M/F): ').strip().upper()
while sex != 'M' and sex != 'F':
    sex = input('Sexo inválido. Digite o sexo da pessoa (M/F): ').strip().upper()

if sex == 'M':
    print('A pessoa é do sexo masculino')
else:
    print('A pessoa é do sexo feminino')


# método do Guanabara
sex = input('digite o sexo da pessoa (M/F): ').strip().upper()[0]
while sex not in 'MmFf':
    sex = input('Sexo inválido. Digite o sexo da pessoa (M/F): ').strip().upper()

if sex == 'M':
    print('A pessoa é do sexo masculino')
else:
    print('A pessoa é do sexo feminino')