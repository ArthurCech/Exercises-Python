# escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1- binário
# 2- octal
# 3- hexadecimal

number = int(input('digite um número inteiro: '))
print('''ESCOLHA A BASE DE CONVERSÃO:
( 1 ) - Binário
( 2 ) - Octal
( 3 ) - Hexadecimal''')
option = int(input('digite a opção: '))

if option == 1:
    print('{}'.format(bin(number)[2:]))
elif option == 2:
    print('{}'.format(oct(number)[2:]))
elif option == 3:
    print('{}'.format(hex(number)[2:]))
else:
    print('Opção inválida!')
