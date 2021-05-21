# faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(phrase):
    tam = len(phrase) + 4
    print('-' * tam)
    print(f'  {phrase}')
    print('-' * tam)


phrase = input('digite uma frase qualquer: ')

escreva(phrase)
