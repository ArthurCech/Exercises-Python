# crie um programa que leia o nome completo de uma pessoa e mostre:
# A) o nome com todas as letras maiúsculas
# B) o nome com todas as letras minúsculas
# C) quantas letras ao todo (sem considerar espaços)
# D) quantas letras tem o primeiro nome

fullName = input('digite o nome completo da pessoa: ')

print('\033[1;33mNome com letras maiúsculas: \033[1;31m{}\033[m'.format(fullName.upper()))
print('\033[1;33mNome com letras minúsculas: \033[1;31m{}\033[m'.format(fullName.lower()))
print('\033[1;33mQtd. de letras: \033[1;31m{}\033[m'.format(len(fullName) - fullName.count(' ')))
print('\033[1;33mQtd. de letras primeiro nome: \033[1;31m{}\033[m'.format(fullName.find(' ')))

# outra forma qtd. de letras do primeiro nome
splitedFullName = fullName.split()
print('\033[1;33mQtd. de letras primeiro nome: \033[1;31m{}\033[m'.format(len(splitedFullName[0])))
