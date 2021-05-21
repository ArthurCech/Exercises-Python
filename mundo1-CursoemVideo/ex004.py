# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

phrase = input('digite a frase: ')

print('Tipo primitivo: {}'.format(type(phrase)))
print('Espaços? {}'.format(phrase.isspace()))
print('Capitalizado? {}'.format(phrase.istitle()))
print('Letras maiúsculas? {}'.format(phrase.isupper()))
print('Letras minúsculas? {}'.format(phrase.islower()))
print('Numérico? {}'.format(phrase.isnumeric()))
print('Alfabético? {}'.format(phrase.isalpha()))
print('Alfanumérico? {}'.format(phrase.isalnum()))
