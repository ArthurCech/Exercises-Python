# faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

name = input('digite o nome completo da pessoa: ').strip()

splitedName = name.split()

print('\033[1;33mPrimeiro nome: \033[1;31m{}\033[m'.format(splitedName[0]))
print('\033[1;33mÚltimo nome: \033[1;31m{}\033[m'.format(splitedName[len(splitedName) - 1]))
