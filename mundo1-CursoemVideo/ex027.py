# faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

name = input('digite o nome completo: ').strip()

name_splited = name.split()

print('Primeiro nome: {}'.format(name_splited[0]))
print('Último nome: {}'.format(name_splited[len(name_splited) - 1]))
