# o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos 
# dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

nome1 = input('nome do 1º aluno: ')
nome2 = input('nome do 2º aluno: ')
nome3 = input('nome do 3º aluno: ')
nome4 = input('nome do 4º aluno: ')

listaAlunos = [nome1, nome2, nome3, nome4]
shuffle(listaAlunos)

print('\033[1;32mOrdem das apresentações: {}\033[m'.format(listaAlunos))
