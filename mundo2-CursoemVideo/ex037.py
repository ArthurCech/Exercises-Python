# escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal, 3 para hexadecimal

number = int(input('digite um número inteiro: '))
print('''BASES DE CONVERSÃO:
(1) - binário
(2) - octal
(3) - hexadecimal''')
option = int(input('digite a opção desejada: '))

if option == 1:
    print('binário: {}'.format(bin(number)[2:]))
elif option == 2:
    print('octal: {}'.format(oct(number)[2:]))
elif option == 3:
    print('hexadecimal: {}'.format(hex(number)[2:]))
else:
    print('opção inválida!')
