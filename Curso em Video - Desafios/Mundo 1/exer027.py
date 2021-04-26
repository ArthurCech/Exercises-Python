# faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o 
# primeiro e o último nome separadamente

name = input('digite o nome completo: ').strip()

nameSplited = name.split()
firstName = nameSplited[0]
lastName = nameSplited[len(nameSplited) - 1]

print('\033[1;33mPrimeiro nome: {}\033[m'.format(firstName))
print('\033[1;34mÚltimo nome: {}\033[m'.format(lastName))
