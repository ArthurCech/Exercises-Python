# crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

students = list()

while True:
    name = input('digite o nome do aluno: ')
    grade1 = float(input('digite a 1ª nota do aluno: '))
    grade2 = float(input('digite a 2ª nota do aluno: '))
    
    average = (grade1 + grade2) / 2
    
    students.append([name, [grade1, grade2], average])

    enter_student = input('digitar mais um aluno [S/N]: ').strip().upper()[0]

    if enter_student == 'N':
        break

print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for number, student in enumerate(students):
    print(f'{number:<4}{student[0]:<10}{student[2]:>8.2f}')

while True:
    print('-' * 35)
    number_student = int(input('digite o número do aluno que deseja mostrar as notas (999 para sair): '))
    
    if number_student == 999:
        break
    elif number_student <= len(students) - 1:
        print(f'Notas de {students[number_student][0]} são {students[number_student][1]}')
