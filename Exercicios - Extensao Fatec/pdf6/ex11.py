from random import randint

print('exercício 11')

quantity = int(input('digite a quantidade de elementos: '))

while quantity <= 0:
    quantity = int(input('[ERRO] digite a quantidade de elementos: '))

list_numbers = []

for count in range(quantity):
    number = randint(0, 1000)
    list_numbers.append(number)

print('Lista: {}'.format(list_numbers))

delete_number = int(input('digite o número que deseja deletar (-1 para sair): '))

while delete_number >= 0:
    if delete_number in list_numbers:
        while delete_number in list_numbers:
            pos = list_numbers.index(delete_number)
            del(list_numbers[pos])

    delete_number = int(input('digite o número que deseja deletar (-1 para sair): '))

print('Lista final: {}'.format(list_numbers))

print('fim do programa')
