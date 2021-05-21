# crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico

def leiaInt(message):
    flag = False
    value = 0
    
    while True:
        number = str(input(message))

        if number.isnumeric():
            value = int(number)
            flag = True
        else:
            print(f'\033[0;31m[ERRO] digite um numéro inteiro válido\033[m')
        if flag:
            break
    return value


number = leiaInt('digite um número: ')
print(f'Você digitou o número {number}')
