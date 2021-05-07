from random import randint

print('exercício 10')

quantity = int(input('digite a quantidade de elementos: '))

while quantity <= 0:
    quantity = int(input('[ERRO] digite a quantidade de elementos: '))

list_numbers = []

for count in range(quantity):
    number = randint(0, 1000)
    list_numbers.append(number)

print('Lista: {}'.format(list_numbers))

search_number = int(input('digite o número que deseja saber se está na lista (-1 para sair): '))

while search_number >= 0:
    find_number = False

    for i in range(len(list_numbers)):
        if search_number == list_numbers[i]:
            print('{} está na lista na posição {}'.format(search_number, count))
            find_number = True
    if find_number == False:
        print('{} não está na lista'.format(search_number))

    search_number = int(input('digite o número que deseja saber se está na lista (-1 para sair): '))

print('fim do programa')
