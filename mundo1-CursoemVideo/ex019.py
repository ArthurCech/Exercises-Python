# um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

from random import choice

name_student_1 = input('digite o nome do 1º estudante: ')
name_student_2 = input('digite o nome do 2º estudante: ')
name_student_3 = input('digite o nome do 3º estudante: ')
name_student_4 = input('digite o nome do 4º estudante: ')

students = [name_student_1, name_student_2, name_student_3, name_student_4]

chosen_student = choice(students)

print('Aluno escolhido: {}'.format(chosen_student))
