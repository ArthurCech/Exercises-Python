print('exercício 4')

# from random import randint

list_numbers_a = []
count = 0

while count < 10:
    number = int(input('digite um número inteiro: '))
    # number = randint(0, 100)
    list_numbers_a.append(number)
    count += 1

list_numbers_b = []
count = 0

while count < 10:
    number = int(input('digite um número inteiro: '))
    # number = randint(0, 100)
    list_numbers_b.append(number)
    count += 1

list_numbers_a_plus_b = list_numbers_a.copy()
list_numbers_a_plus_b.extend(list_numbers_b)

print('Lista resultante = {}'.format(list_numbers_a_plus_b))

print('fim do programa')
