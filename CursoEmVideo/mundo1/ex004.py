# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela

phrase = input('digite uma frase: ')

print('\033[1;33mTipo: \033[1;31m{}\033[m'.format(type(phrase)))
print('\033[1;33mNumérico: \033[1;31m{}\033[m'.format(phrase.isnumeric()))
print('\033[1;33mAlfanumérico: \033[1;31m{}\033[m'.format(phrase.isalnum()))
print('\033[1;33mAlfabético: \033[1;31m{}\033[m'.format(phrase.isalpha()))
print('\033[1;33mLetras maiúsculas: \033[1;31m{}\033[m'.format(phrase.isupper()))
print('\033[1;33mLetras minúsculas: \033[1;31m{}\033[m'.format(phrase.islower()))
print('\033[1;33mCapitalizado: \033[1;31m{}\033[m'.format(phrase.istitle()))
print('\033[1;33mEspaço em branco: \033[1;31m{}\033[m'.format(phrase.isspace()))
