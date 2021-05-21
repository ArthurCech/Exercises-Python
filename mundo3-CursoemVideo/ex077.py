# crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar para cada palavra, quais são suas vogais

words = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
         'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for word in words:
    print('Palavra: {} - Vogais: '.format(word.upper()), end = '')

    for letter in word:
        if letter in 'aeiou':
            print('{}  '.format(letter), end = '')
    
    print()
