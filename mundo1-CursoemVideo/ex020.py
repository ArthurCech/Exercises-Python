# o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

name_student_1 = input('digite o nome do 1º estudante: ')
name_student_2 = input('digite o nome do 2º estudante: ')
name_student_3 = input('digite o nome do 3º estudante: ')
name_student_4 = input('digite o nome do 4º estudante: ')

students = [name_student_1, name_student_2, name_student_3, name_student_4]

shuffle(students)

print('Ordem de apresentação: {}'.format(students))
