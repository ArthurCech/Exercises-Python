print('exercício 1')

first_term = int(input('digite o primeiro termo da PG: '))
common_difference = int(input('digite a razão da PG: '))
quantity = int(input('digite a quantidade de termos da PG: '))

count = 0

while count < quantity:
    print(first_term, end=' ')
    first_term = first_term * common_difference
    count += 1
    
print('\nfim do programa')
