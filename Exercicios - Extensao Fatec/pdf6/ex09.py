from random import randint

print('exercício 9')

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
    if search_number in list_numbers:
        print('O número {} está na lista'.format(search_number))
    else:
        print('O número {} não está na lista'.format(search_number))

    search_number = int(input('digite o número que deseja saber se está na lista (-1 para sair): '))

print('fim do programa')
