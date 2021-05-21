# crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

phrase = input('digite a frase: ').strip().lower()

phrase_splited = phrase.split()

final_phrase = ''.join(phrase_splited)

reversed_phrase = ''

for letter in range(len(final_phrase) -1, -1, -1):
    reversed_phrase += final_phrase[letter]

print('O inverso de {} é {}'.format(final_phrase, reversed_phrase))

if reversed_phrase == final_phrase:
    print('{} é um palíndromo'.format(final_phrase))
else:
    print('{} não é um palíndromo'.format(final_phrase))
