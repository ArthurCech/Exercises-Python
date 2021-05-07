print('exercício 3')

first_number = int(input('digite o 1º número inteiro: '))
second_number = int(input('digite o 2º número inteiro: '))

if first_number > second_number:
    print('O maior número é o 1º ({})'.format(first_number))
    print('O menor número é o 2º ({})'.format(second_number))
elif second_number > first_number:
    print('O maior número é o 2º ({})'.format(second_number))
    print('O menor número é o 1º ({})'.format(first_number))
else:
    print('Os numeros informados são iguais ({} e {})'.format(first_number, second_number))
    
print('fim do programa')
