# crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida
# -média abaixo de 5.0: REPROVADO
# -média entre 5.0 e 6.9: RECUPERAÇÃO
# -média 7.0 ou superior: APROVADO

grade1 = float(input('digite a 1ª nota: '))
grade2 = float(input('digite a 2ª nota: '))

average = (grade1 + grade2) / 2

if average < 5:
    print('Média: {:.2f} - REPROVADO'.format(average))
elif average < 6.9:
    print('Média: {:.2f} - RECUPERAÇÃO'.format(average))
else:
    print('Média: {:.2f} - APROVADO'.format(average))
