# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

text = input('digite alguma coisa: ')

print('Tipo primitivo da variável: {}'.format(type(text))) # tipo
print('É numérico? {}'.format(text.isnumeric())) # numérico
print('É alfabético? {}'.format(text.isalpha())) # alfabético
print('É alfanumérico? {}'.format(text.isalnum())) # alfanumérico
print('É uppercase? {}'.format(text.isupper())) # uppercase
print('É lowercase? {}'.format(text.islower())) # lowercase
print('É title? {}'.format(text.istitle())) # letras maiúsculas
print('É um espaço em branco? {}'.format(text.isspace())) # espaço em branco
