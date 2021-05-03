# o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

name1 = input('digite o nome do 1º aluno: ').strip()
name2 = input('digite o nome do 2º aluno: ').strip()
name3 = input('digite o nome do 3º aluno: ').strip()
name4 = input('digite o nome do 4º aluno: ').strip()

listStudents = [name1, name2, name3, name4]
shuffle(listStudents)

print('\033[1;33mOrdem de apresentação: \033[1;31m{}\033[m'.format(listStudents))
