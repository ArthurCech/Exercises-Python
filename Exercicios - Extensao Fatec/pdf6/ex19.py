print('exercício 19')

list_numbers = []

number = int(input('digite um número inteiro: '))

while number > 0:
    i = 0

    while i < len(list_numbers) and number > list_numbers[i]:
        i += 1
        
    if number > 0:
        list_numbers.insert(i, number)
    
    number = int(input('digite um número inteiro: '))

print('Lista: {}'.format(list_numbers))

print('fim do programa')
