# escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher 
# qual será a base de conversão

number = int(input('digite um número inteiro qualquer: '))
print('''BASES DE CONVERSÃO:
( 1 ) binário
( 2 ) octal
( 3 ) hexadecimal''')
option = int(input('digite a opção desejada: '))

if option == 1:
    print('{} decimal = {} binário'.format(number, bin(number)[2:]))
elif option == 2:
    print('{} decimal = {} octal'.format(number, oct(number)[2:]))
elif option == 3:
    print('{} decimal = {} hexadecimal'.format(number, hex(number)[2:]))
else:
    print('Opção inválida')

# [2:] para remover os 2 primeiros caracteres que simbolizam o tipo, como:
# 0x: hexadecimal | 0o: octal | 0b: binário
