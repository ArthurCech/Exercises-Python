print('exercício 3')

list_numbers = []
count = 0

while count < 10:
    number = int(input('digite um número inteiro: '))
    list_numbers.append(number)
    count += 1

list_numbers.reverse()

print('Lista criada = {}'.format(list_numbers))

print('fim do programa')
