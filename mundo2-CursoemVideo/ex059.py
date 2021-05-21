# crie um programa que leia dois valores e mostre um menu. Seu programa deverá realizar a operação solicitada em cada caso. [1] - somar; [2] - multiplicar; [3] - maior; [4] - novos números; [5] - sair do programa

number1 = int(input('digite o 1ª número: '))
number2 = int(input('digite o 2º número: '))
operation = 0

while operation != 5:
    print('''ESCOLHA UMA OPÇÃO:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    operation = int(input('digite a operação desejada: '))

    if operation == 1:
        sum_numbers = number1 + number2
        print('{} + {} = {}'.format(number1, number2, sum_numbers))
    elif operation == 2:
        mult_numbers = number1 * number2 
        print('{} * {} = {}'.format(number1, number2, mult_numbers))
    elif operation == 3:
        if number1 > number2:
            print('O 1º número é o maior ({})'.format(number1))
        elif number2 > number1:
            print('O 2º número é o maior ({})'.format(number2))
        else:
            print('Os números são iguais ({} = {})'.format(number1, number2))
    elif operation == 4:
        number1 = int(input('digite o 1ª número: '))
        number2 = int(input('digite o 2º número: '))
    elif operation == 5:
        print('finalizando o programa')
    else:
        print('operação inválida, digite novamente!')
