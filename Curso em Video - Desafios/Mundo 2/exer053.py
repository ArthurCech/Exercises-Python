# crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
# desconsiderando os espaços

phrase = input('digite uma frase: ').strip().lower()

# remover espaços em branco
words = phrase.split()
phraseNoBlank = ''.join(words)

reversedPhrase = ''
for letter in range(len(phraseNoBlank) - 1, - 1, - 1):
    reversedPhrase += phraseNoBlank[letter]

if reversedPhrase == phraseNoBlank:
    print('{} é um palíndromo'.format(phrase))
else:
    print('{} não é palíndromo'.format(phrase))
    