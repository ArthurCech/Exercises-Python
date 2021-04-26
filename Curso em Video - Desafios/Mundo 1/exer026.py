# faça um programa que leia uma frase pelo teclado e mostre:
# - quantas vezes aparece a letra "a"
# - em que posição ela aparece a primeira vez
# - em que posição ela aparece a última vez

frase = input('digite uma frase: ').strip().lower()

qtdLetterA = frase.count('a')
firstLetterA = frase.find('a')
lastLetterA = frase.rfind('a')

print('\033[1;33mQtd. de letras "a": {}\033[m'.format(qtdLetterA))
print('\033[1;34mPrimeira vez que aparece a letra "a": {}\033[m'.format(firstLetterA))
print('\033[1;35mUltima vez que aparece a letra "a": {}\033[m'.format(lastLetterA))
