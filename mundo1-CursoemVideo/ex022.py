# crie um programa que leia o nome completo de uma pessoa e mostre:
# -o nome com todas as letras maiúsculas e minúsculas
# -quantas letras ao todo (sem considerar espaços)
# -quantas letras tem o primeiro nome

name = input('digite o nome completo: ').strip()

print('Nome em maiúsculas: {}'.format(name.upper()))
print('Nome em minúsculas: {}'.format(name.lower()))
print('Qtd. de letras: {}'.format(len(name) - name.count(' ')))
print('Qtd. de letras do primeiro nome: {}'.format(name.find(' ')))

# outra forma para qtd. de letras do primeiro nome
name_splited = name.split()
print('Qtd. de letras do primeiro nome: {}'.format(len(name_splited[0])))
