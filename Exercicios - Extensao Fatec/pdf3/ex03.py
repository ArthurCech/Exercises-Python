print('exercício 3')

quantity = int(input('digite a quantidade de números reais: '))

count = sum_float_number = 0

while count < quantity:
    number = float(input('digite um número real: '))
    sum_float_number += number
    count += 1

print('Soma dos valores digitados = {}'.format(sum_float_number))

print('fim do programa')
