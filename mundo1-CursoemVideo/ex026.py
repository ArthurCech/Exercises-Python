# faça um programa que leia uma frase pelo teclado e mostre:
# -quantas vezes aparece a letra "A"
# -em que posição ela aparece a primeira vez
# -em que posição ela aparece a última vez

phrase = input('digite a frase: ').strip().upper()

print('Qtd. de letras A: {}'.format(phrase.count('A')))
print('Primeira aparição da letra A: {}'.format(phrase.find('A')))
print('Última aparição da letra A: {}'.format(phrase.rfind('A')))
