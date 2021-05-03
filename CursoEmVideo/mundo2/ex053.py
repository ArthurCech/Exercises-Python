# crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

phrase = input('digite uma frase: ').strip().upper()

words = phrase.split()
newPhrase = ''.join(words)
reversedPhrase = newPhrase[::-1]

print('Inverso de {} = {}'.format(newPhrase, reversedPhrase))

if reversedPhrase == newPhrase:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
