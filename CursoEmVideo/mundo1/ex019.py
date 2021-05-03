# um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

name1 = input('digite o nome do 1º aluno: ').strip()
name2 = input('digite o nome do 2º aluno: ').strip()
name3 = input('digite o nome do 3º aluno: ').strip()
name4 = input('digite o nome do 4º aluno: ').strip()

listStudents = [name1, name2, name3, name4]
chosenStudent = choice(listStudents)

print('\033[1;33mAluno escolhido: \033[1;31m{}\033[m'.format(chosenStudent))
