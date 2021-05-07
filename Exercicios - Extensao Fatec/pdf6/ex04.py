from random import randint

print('exercício 4')

quantity = int(input('digite a quantidade de elementos (entre 1 e 50): '))

while quantity <= 0 or quantity > 50:
    quantity = int(input('[ERRO] digite a quantidade de elementos (entre 1 e 50): '))

list_numbers = []

for count in range(quantity):
    number = randint(0, 1000)
    list_numbers.append(number)

print('Lista:')

for number in list_numbers:
    print(number)

print('fim do programa')
