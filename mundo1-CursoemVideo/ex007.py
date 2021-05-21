# desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

grade1 = float(input('digite a 1ª nota: '))
grade2 = float(input('digite a 2ª nota: '))

average = (grade1 + grade2) / 2

print('Média do aluno: {:.2f}'.format(average))
