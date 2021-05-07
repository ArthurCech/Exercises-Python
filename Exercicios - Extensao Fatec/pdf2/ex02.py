print('exercício 2')

first_number = int(input('digite o 1º número inteiro: '))
second_number = int(input('digite o 2º número inteiro: '))

if first_number < second_number:
    print('O menor número é o primeiro ({})'.format(first_number))
elif second_number < first_number:
    print('O menor número é o segundo ({})'.format(second_number))
else:
    print('Os números são iguais ({} e {})'.format(first_number, second_number))

print('fim do programa')
