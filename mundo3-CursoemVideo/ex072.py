# crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número (entre 0 e 20) e mostrá-lo por extenso

numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

number = int(input('digite um número entre 0 e 20: '))
while number < 0 or number > 20:
    number = int(input('[ERRO] digite um número entre 0 e 20: '))

print(f'Você digitou o número {numbers[number]}')




# MÉTODO 2
numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    number = int(input('digite um número entre 0 e 20: '))

    if 0 <= num <= 20:
        break

print(f'Você digitou o número {numbers[number]}')
