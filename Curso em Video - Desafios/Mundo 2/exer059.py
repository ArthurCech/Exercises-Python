# crie um programa que leia dois valores e mostre um menu na tela
# [1] - somar
# [2] - multiplicar
# [3] - maior
# [4] - novos números
# [5] - sair do programa
# seu programa deverá realizar a operação solicitada em cada caso

number1 = int(input('digite o 1º número: '))
number2 = int(input('digite o 2º número: '))

option = 1
while option > 0 and option < 5:
    print('''OPERAÇÕES:
[1] - somar
[2] - multiplicar
[3] - maior
[4] - novos números
[5] - sair do programa''')
    option = int(input('digite a opção da operação desejada: '))

    if option == 1: # somar
        sumNumbers = number1 + number2
        print('\033[1;33mSoma dos números: {}\033[m'.format(sumNumbers))
    elif option == 2: # multiplicar
        multNumbers = number1 * number2
        print('\033[1;33mMultiplicação dos números: {}\033[m'.format(multNumbers))
    elif option == 3: # maior
        if number1 > number2:
            print('\033[1;33m1º número ({}) é maior que o 2º número ({})\033[m'.format(number1, number2))
        elif number2 > number1:
            print('\033[1;33m2º número ({}) é maior que o 1º número ({})\033[m'.format(number2, number1))
        else:
            print('\033[1;33mOs números são iguais ({} {})\033[m'.format(number1, number2))
    elif option == 4:
            number1 = int(input('digite o 1º número: '))
            number2 = int(input('digite o 2º número: '))
    elif option == 5:
        print('finalizando programa...')
    else:
        print('opção inválida')
