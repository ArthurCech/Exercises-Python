# faça um programa que leia nome e média de um aluno, guardando também a situação (média >= 7 aprovad) em um dicionário. No final, mostre o conteúdo da estrutura na tela

student = dict()

student['nome'] = input('digite o nome do estudante: ')
student['media'] = float(input('digite a média do estudante: '))

if student['media'] >= 7:
    student['situacao'] = 'Aprovado'
elif student['media'] >= 5:
    student['situacao'] = 'Recuperação'
else:
    student['situacao'] = 'Reprovado'

for key, value in student.items():
    print(f'{key}: {value}')
