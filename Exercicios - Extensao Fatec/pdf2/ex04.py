print('exercício 4')

number = int(input('digite um número inteiro: '))

if number == 0:
    print('O número {} é zero'.format(number))
elif number % 2 == 0:
    print('O número {} é par'.format(number))
else:
    print('O número {} é ímpar'.format(number))
    
print('fim do programa')
