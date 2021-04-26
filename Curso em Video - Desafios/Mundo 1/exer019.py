# um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um 
# programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

nome1 = input('digite o nome do 1º aluno: ')
nome2 = input('digite o nome do 2º aluno: ')
nome3 = input('digite o nome do 3º aluno: ')
nome4 = input('digite o nome do 4º aluno: ')

listaAlunos = [nome1, nome2, nome3, nome4]
alunoEscolhido = choice(listaAlunos)

print('\033[1;32mAluno escolhido: {}\033[m'.format(alunoEscolhido))
