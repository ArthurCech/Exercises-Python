# crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida: média abaixo de 5.0 - reprovado; média entre 5.0 e 6.9 - recuperação; média 7.0 ou superior - aprovado

grade1 = float(input('digite a 1ª nota: '))
grade2 = float(input('digite a 2ª nota: '))

average = (grade1 + grade2) / 2

if average < 5:
    print('REPROVADO')
elif average < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
