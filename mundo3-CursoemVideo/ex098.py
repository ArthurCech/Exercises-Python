# faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada: A) de 1 até 10, de 1 em 1; B) de 10 até 0; de 2 em 2; C) uma contagem personalizada

def contador(first, last, common_diff):
    if common_diff < 0:
        common_diff *= -1
    if common_diff == 0:
        common_diff = 1

    print('-=-' * 20)
    print(f'iniciando contagem de {first} até {last} utilizando razão de {common_diff}')
    
    if first < last:
        for number in range(first, last + 1, common_diff):
            print(f'{number} ', end='')
        print()
    else:
        for number in range(first, last - 1, -common_diff):
            print(f'{number} ', end='')
        print()
    

contador(1, 10, 1)
contador(10, 0, 2)

first = int(input('digite o valor inicial: '))
last = int(input('digite o valor final: '))
common_diff = int(input('digite a razão: '))

contador(first, last, common_diff)
