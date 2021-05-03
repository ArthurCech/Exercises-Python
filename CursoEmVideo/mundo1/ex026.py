# faça um programa que leia uma frase pelo teclado e mostre:
# A) quantas vezes aparece a letra "A"
# B) em que posição ela aparece a primeira vez
# C) em que posição ela aparece a última vez

phrase = input('digite uma frase qualquer: ').strip().upper()

print('\033[1;33mQtd. de letras "A": \033[1;31m{}\033[m'.format(phrase.count('A')))
print('\033[1;33mPosição que aparece o 1º "A": \033[1;31m{}\033[m'.format(phrase.find('A')))
print('\033[1;33mPosição que aparece o último "A": \033[1;31m{}\033[m'.format(phrase.rfind('A')))
