# crie um programa que leia o nome completo de uma pessoa e mostre:
# - o nome com todas as letras maiúsculas e minúsculas
# - quantas letras ao todo (sem considerar espaços)
# - quantas letras tem o primeiro nome

name = input('digite o nome completo: ').strip()

print('\033[1;33mNome em maiúsculas: {}\033[m'.format(name.upper()))
print('\033[1;34mNome em minúsculas: {}\033[m'.format(name.lower()))
print('\033[1;35mQtd. de letras do nome completo: {}\033[m'.format(len(name) - name.count(' ')))
print('\033[1;36mQtd. de letras do primeiro nome: {}\033[m'.format(name.find(' ')))

# outra forma para contar as letras do primeiro nome
nameSplited = name.split()
print('\033[1;30mO primeiro nome é {} e tem {} letras\033[m'.format(nameSplited[0], len(nameSplited[0])))
