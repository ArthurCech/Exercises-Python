# crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma 
# mensagem no final, de acordo com a média atingida:
# - abaixo de 5.0: REPROVADO
# - entre 5.0 e 6.9: RECUPERAÇÃO
# - acima de 7.0: APROVADO

grade1 = float(input('digite a nota 1: '))
grade2 = float(input('digite a nota 2: '))

average = (grade1 + grade2) / 2

print('Média = {:.2f}'.format(average))

if average < 5.0:
    print('REPROVADO')
elif average < 7.0:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
